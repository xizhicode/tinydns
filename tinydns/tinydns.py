# coding:utf-8
# write by zhou
__doc__ = """tinydns , is a base on gevent tiny dns server .
Usage:
  tinydns (-c <config_path>| -h )

Options:
  -h --help       show the help info. 
  -c --conf       specify the config file . example /etc/tinydns.conf
"""
import docopt
from gevent import monkey
monkey.patch_all()
from .log import get_logger
from gevent import socket
import gevent
from dnslib import *
from .daemon import daemon_start
import re
try:
    import ConfigParser as configparser
except:
    import configparser
from .cache import DnsRecordCache
import dns.resolver


_config_path = None
_last_read_time = 0
_config_cache = None
try:
    logger = get_logger('/tmp/tinydns.log',3)
except:
    logger = None
query_cache = DnsRecordCache(20)


def log(message):
    if logger:
        logger.info(message)


def _conf_handle(conf_dict):
    buff = []
    for key,value in conf_dict.items():
        value = value.strip()
        _ = value.split(",")
        _ = [i for i in _ if re.match(
                r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$",i)]
        buff.append((key,_))
    return dict(buff)


def get_addr_from_conf(qname):
    global _config_cache, _last_read_time, _config_path
    other_qname = ''
    try:
        other_qname = ".".join(["*"] + qname.split(".")[1:])
    except:
        pass
    if not _config_path:
        return None
    else:
        if time.time() - _last_read_time > 1:
            cf = configparser.ConfigParser()
            try:
                cf.read(_config_path)
                try:
                    _config_cache = _conf_handle(dict(cf.items('tinydns')))
                except configparser.NoSectionError:
                    _config_cache = {}
            except:
                pass
            _last_read_time = time.time()
        _ = _config_cache.get(qname) or _config_cache.get(other_qname)
        if _:
            return random.choice(_)
        else:
            return None


def dns_handler(s, peer, data):
    request = DNSRecord.parse(data)
    id = request.header.id
    qname = request.q.qname
    qtype = request.q.qtype
    _qname =  str(qname)[:-1] if str(qname).endswith(".") else str(qname)
    reply = DNSRecord(DNSHeader(id=id, qr=1, aa=1, ra=1), q=request.q)
    if qtype == QTYPE.A:
        _ = get_addr_from_conf(_qname)
        if not _:
            _c_ = query_cache.get(_qname)
            if _c_:
                result_ip = _c_
            else:
                try:
                    with gevent.Timeout(5):
                        result_ip = dns.resolver.query(str(_qname),"A").response.answer[-1].items[-1].address
                        query_cache.add(_qname, result_ip)
                except dns.resolver.NXDOMAIN:
                        result_ip = dns.resolver.NXDOMAIN
                        query_cache.add(_qname, result_ip)
                except (BaseException,Exception, gevent.Timeout) as e:
                    result_ip = None
                    log("%s getaddr failed %s" % (str(qname),str(e)))
        else:
            result_ip = _
        if result_ip and result_ip != dns.resolver.NXDOMAIN:
            reply.add_answer(RR(qname, qtype, rdata=A(result_ip)))
            log('receive query, qname: %s  qtype: %s . reply %s' % (str(qname), QTYPE[qtype],result_ip))
        else:
            reply.header.rcode = RCODE.NXDOMAIN
            log('receive query, qname: %s  qtype: %s . reply NXDOMAIN' % (str(qname), QTYPE[qtype]))

    else:
        log('receive query, qname: %s  qtype: %s . empty reply' % (str(qname), QTYPE[qtype]))
    s.sendto(reply.pack(), peer)


def main():
    global _config_path,_config_cache
    argument = docopt.docopt(__doc__)
    config_path = argument["<config_path>"]
    try:
        config_path = config_path.strip()
        assert config_path
        cf = configparser.ConfigParser()
        cf.read(config_path)
        try:
            _config_cache = _conf_handle(dict(cf.items('tinydns')))
            _last_read_time = time.time()
        except configparser.NoSectionError:
            _config_cache = {}
    except:
        print("error! cant read %s!" % config_path)
    _config_path = config_path
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('0.0.0.0', 53))
    log('start success...')
    print('start success...')
    daemon_start()
    while True:
        data, peer = s.recvfrom(8192)
        gevent.spawn(dns_handler, s, peer, data)