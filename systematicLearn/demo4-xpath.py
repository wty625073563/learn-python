import requests

from lxml import etree

url = 'https://book.douban.com/subject/30232235/comments/'
r = requests.get(url).text

# print(r)

# 获取html
s = etree.HTML(r)

# print(s.xpath('//*[@id="comments"]/ul/li[1]/div[2]/p/span/text()')) #浏览器复制

print(s.xpath('//p[@class="comment-content"]/span/text()')[0])