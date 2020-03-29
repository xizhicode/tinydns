# coding:utf-8
# write by zhou
import dns.resolver


try:
    q = dns.resolver.query("aaa.wolover123.com","A")
except dns.resolver.NXDOMAIN:
    q = "fdsa"

print(q)