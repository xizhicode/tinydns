# coding:utf-8
from gevent import monkey
monkey.patch_all()
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
    tt = gevent.joinall([gevent.spawn(test,'zhplz.co')  for i in range(100)])
