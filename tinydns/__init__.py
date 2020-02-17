# -*- coding: utf-8 -*-
import argparse
from gevent import socket
import gevent
from gevent import monkey
monkey.patch_socket()
from dnslib import *
try:
    import ConfigParser
except:
    import configparser
import shutil
from pkg_resources import Requirement, resource_filename


def dns_handler(s, peer, data):
    request = DNSRecord.parse(data)
    id = request.header.id
    qname = request.q.qname
    qtype = request.q.qtype
    try:
        IP = socket.gethostbyname(str(qname))
    except Exception as e:
        IP = '0.0.0.0'
    print ("request:%s:%s -- response: %s" % (str(peer), qname.label, IP))
    reply = DNSRecord(DNSHeader(id=id, qr=1, aa=1, ra=1), q=request.q)
    if qtype == QTYPE.A:
        reply.add_answer(RR(qname, qtype, rdata=A(IP)))
    elif qtype == QTYPE['*']:
        reply.add_answer(RR(qname, QTYPE.A, rdata=A(IP)))
        reply.add_answer(RR(qname, QTYPE.MX, rdata=MX(IP)))
        reply.add_answer(RR(qname, QTYPE.TXT, rdata=TXT(TXT)))
    else:
        reply.add_answer(RR(qname, QTYPE.CNAME, rdata=CNAME(TXT)))
    s.sendto(reply.pack(), peer)


def main():
    # filename = resource_filename(Requirement.parse("tinydns"), "etc/tinydns.conf")
    # target = '/etc/tinydns.conf'
    # try:
    #     shutil.copyfile(filename, target)
    # except IOError as e:
    #     print("Unable to copy file. %s" % e)
    try:
        parser = argparse.ArgumentParser(description='Run some watchers.')
        parser.add_argument('-c', action='store_true',help="Run service command tinydns -c /etc/tinydns.conf")
        parser.add_argument('-m', help="Requires configuration in /etc/tinydns.conf [gevent_dns]AF_INET = 2 SOCK_DGRAM = 2 port = 53")
        parser.add_argument('filename',help='Please enter a file name')
        args = parser.parse_args()
        con_cig = os.path.join(args.filename)
        try:
            cf = ConfigParser.ConfigParser()
        except:
            cf = configparser.ConfigParser()
        try:
            cf.read(con_cig)
            AF_INET = cf.get('gevent_dns', 'AF_INET')
            SOCK_DGRAM = cf.get('gevent_dns', 'AF_INET')
            port = cf.get('gevent_dns', 'port')
        except Exception as e:
            AF_INET = 2
            SOCK_DGRAM = 2
            port = 53
        s = socket.socket(int(AF_INET), int(SOCK_DGRAM))
        s.bind(('', int(port)))
    except Exception as e:
        print ('Switch root permissions run service command tinydns -c /etc/tinydns.conf')
    else:
        while True:
            data, peer = s.recvfrom(8192)
            gevent.spawn(dns_handler, s, peer, data)


if __name__ == '__main__':
    main()