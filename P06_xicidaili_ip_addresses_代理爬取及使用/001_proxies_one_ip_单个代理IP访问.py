# -*- coding: utf-8 -*-

# 单个IP代理设置方式

# 使用HTTP和HTTPS可以正常访问,http也可以，就是https不能访问，

import requests

proxies = {
    'http': '112.85.170.133:9999',
    'https': '112.85.170.133:9999',
}

url = 'https://www.hao123.com/'
response = requests.get(url, proxies=proxies)  #verify=False是否验证服务器的SSL证书

print(response.status_code)
print(response.headers)