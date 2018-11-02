# -*- coding=utf-8 -*-

import requests

url = 'https://oss.ibos.cn/common/json/card/appLink.json?timestamp=1541068159805'

header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}
r = requests.get(url).json()

print(r)