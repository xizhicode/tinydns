# coding:utf-8
# write by zhou
import time
from collections import OrderedDict

class DnsRecordCache(object):
    # dns record cache
    def __init__(self,size=20000, ttl=3):
        self.size = size
        self.ttl = ttl
        self._s = OrderedDict()
        self._size = 0

    def add(self, qname, ip):
        if self._size < self.size:
            pass
        else:
            self._s.popitem(False)
            self._size -= 1
        if not qname in self._s:
            self._size += 1
        self._s[qname] = (ip, time.time())

    def get(self, qname):
        now_time = time.time()
        _ = self._s.get(qname)
        if _:
            ip, _time = _
            if now_time - _time <= self.ttl:
                return ip
        return None


if __name__ == '__main__':
    cache = DnsRecordCache(30000)
    i = 0
    while 1:
        i += 1
        cache.add(str(i),str(i))
        print(i)
        print(cache._size,len(cache._s),cache.get(str(i-29999)),cache.get(str(i-30000)))

