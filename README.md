# tinydns

基于gevent的轻量dns服务

* 依赖的包 gevent,dnslib  python2:ConfigParser python3:configparser

* 方法1： pip install tinydns == 0.0.8

* 方法2： git clone https://github.com/xizhicode/tinydns.git

* 在 /etc 下 配置 tinydns.conf
        [gevent_dns]
        AF_INET = 2
        SOCK_DGRAM = 2
        port = 53
* 运行命令：sudo tinydns -c  /etc/tinydns.conf


* 测试： dig @127.0.0.1 google.com
