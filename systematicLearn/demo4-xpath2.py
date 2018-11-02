import requests
from lxml import etree


def getContent(url, xpath):
    # r = requests.get(url).text
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding

        s = etree.HTML(r.text)
        return s.xpath(xpath)
    except:
        return '异常'
    # print(r)


# 爬百度
def getBaiduXath():
    url = 'http://www.baidu.com/s?ie=UTF-8&wd=%E6%89%8B%E5%86%99xpath'

    print(getContent(url, '//div[@id="1"]/h3/a/text()'))

# github
def getGitHub():
    url = 'https://github.com/Tencent/westore'

    print(getContent(url, '//p/a/img/@src'))

# getGitHub()

def getZhihu():
    urls = ['http://www.zhihu.com', '/topic/19552832/top-answers']
    url = ''.join(urls)
    # 字典
    content = {}
    content['name'] = getContent(url, '//*[@id="TopicMain"]/div/div/div/div[1]/div/h2/div/a/text()')
    content['url'] = urls[0] + (getContent(url, '//*[@id="TopicMain"]/div/div/div/div[1]/div/h2/div/a/@href')[0])

    print(content)

getZhihu()

