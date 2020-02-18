# tinydns


基于gevent异步IO框架实现的轻量DNS服务器，易于配置和启动，可安装于Python2或Python3环境， 可用于爬虫等业务中。



## 1.如何安装


#### 使用pip 安装
```commandline
pip install  tinydns
```


### 2.配置及使用示例

#### 创建配置文件
```commandline
vim /etc/tinydns.conf

```
在文件中输入如下内容：
```commandline
[tinydns]
*.baidu.com = 192.168.1.1,192.168.1.2,192.168.1.3
www.baidu.com  = 192.168.1.4,192.168.1.5
image.baidu.com =  192.168.1.1
```
上面的配置文件所代表的意思是：
 - 所有符合*.baidu.com的域名(除了www.baidu.com image.baidu.com)均随机解析到192.168.1.1 192.168.1.2 192.168.1.3中的随意一个
 - 所有符合www.baidu.com的域名 随机解析到 192.168.1.4 192.168.1.5中的随机一个
 - 所有符合image.baidu.com的域名 解析到 192.168.1.1
 - 除了以上之外的域名则直接从本机网络设置中获取到对应的DNS记录返回给客户端

#### 启动服务
```shell script
tinydns -c /etc/tinydns.conf
```

#### 备注：
如在服务运行中 修改了配置文件 无需重启，服务会自动加载新的配置文件内容。

### 联系我们
周坤朋： <zhoukunpeng504@163.com><br/>
赵恒苹： <18438697706@163.com>
