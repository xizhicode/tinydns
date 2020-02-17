# -*- coding: utf-8 -*-
import os
aa = os.system("dig @127.0.0.1 zhplz.com")
print (aa)

def find_config():
    config_path = 'tinydns.conf'
    if os.path.exists(config_path):
        return config_path
    config_path = os.path.join(os.path.dirname(__file__),'../','tinydns.conf')
    if os.path.exists(config_path):
        return config_path
    return None
