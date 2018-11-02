# encoding='utf-8'

import requests

url = 'http://www.zhihu.com/'
# timeout 超时等待
def getHtmlText(url):
    try:
        r = requests.get(url, timeout=20)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return '异常'

print(__name__)

if __name__ == '__main__':
    url = ''
    print(getHtmlText(url))
# 打印错误
# print(r.raise_for_status())