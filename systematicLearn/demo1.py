# import urllib.request
# f = urllib.request.urlopen('http://www.baidu.com/')
# # print(f.read(500))
# print(f.read(500).decode('utf-8'))

import requests
r = requests.get('https://www.baidu.com/')
# print(r)
# print(r.text)
r.encoding = 'utf-8'
print(r.text)