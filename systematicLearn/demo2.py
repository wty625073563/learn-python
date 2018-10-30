# encoding='utf-8'

import requests
# 获取
r = requests.get('https://book.douban.com/subject/30232235/comments/')
r.encoding = 'utf-8'
# print(r.text)

# 解析
from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, 'lxml')
pattern = soup.find_all('span','short')
print(pattern)
# # 打印数据
for item in pattern:
    print(item.string)

# 保存数据
import pandas
# 新建对象
comments = []
for item in pattern:
    comments.append(item.string)

# 导出前格式化数据
df = pandas.DataFrame(comments)

# 导出csv文件
# df.to_excel('comments.xls')
df.to_csv('comments.csv', encoding='utf_8_sig')