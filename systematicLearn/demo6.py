import requests
import pandas as pd
import time

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}

followers = []

def get_followed(page):
    for i in range(page):
        url = 'https://www.zhihu.com/api/v4/members/sun-yihan-79/followers?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset={}&limit=20'.format(i * 20)
        data = requests.get(url, headers=headers).json()['data'] # 需要获取的元素
        # print(data)
        followers.extend(data)
        # print输出变量 %转换符 s字符串 输出字符串
        print("正在爬取第%s页" % str(i+1))
        time.sleep(1)


if __name__ == '__main__':
    # 加载10页
    get_followed(10)

    # 格式化对象 将followers格式化成dataframe格式
    df = pd.DataFrame.from_dict(followers)
    df.to_csv('zhihu-followers.csv', encoding='utf_8_sig')

