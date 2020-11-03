# coding:utf-8
import dns.resolver


try:
    q = dns.resolver.query("zhplz.com","A")
except dns.resolver.NXDOMAIN:
    q = "解析失败"

print(q)