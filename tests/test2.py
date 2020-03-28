# coding:utf-8
# write by zhou
import docopt
from gevent import monkey
monkey.patch_all()
from gevent.lock import BoundedSemaphore
import  socket
import gevent

def test(domain):
    try:
        with gevent.Timeout(2) as t:
            aa = socket.gethostbyname(domain)
            print(aa)
            return aa
    except (BaseException,Exception) as e :
        print(str(e))


while 1:
    tt = gevent.joinall([gevent.spawn(test,'www.baidu.com')  for i in range(100)])
