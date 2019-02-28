from bs4 import BeautifulSoup
import time,csv
from random import uniform,choice
import requests
from bs4 import BeautifulSoup
import re

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
cities = ['jiangninga','pukou',',jianye','guloua','qinhuai','xuanwub','qixia','yuhuatai','liuhe','lishuia','gaochun']
def get_city():
    global cities
    try:
        city = choice(cities)
        cities.remove(city)
        # 随机选取一个城市进行爬取，然后再列表中删除这个城市
        print(city)
    except IndexError:
        return None
    # 当没有城市了，就返回一个None
    return city

def get_url(city):
    if city == None:
        return
    # 城市值为None时，我们就跳出
    else:
        url = 'https://www.anjuke.com/fangjia/nanjing2019/{city}/'.format(city=city)
        return url

def get_ressponse(url,file,headers):
    html = requests.get(url=url,headers=headers,verify=False)
    Soup = BeautifulSoup(html.text,'lxml')
    #print(Soup.prettify())
    ls = Soup.findAll(name='div', attrs={"class": "sub-items"})
    #print(ls[0])
    try:
        line = str(ls[0])
        #print(line)
        #print(line)
        result = re.findall('<a href="http://www.anjuke.com/fangjia/nanjing2019/(.*?)/">',line,re.S)
        #for i in range(100):
        print(result)
        file.writerow(result)
    except Exception:
        print("Index out of range")

def main(city):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Referer': 'https://www.anjuke.com/fangjia/nanjing2019/{city}/'.format(city=city),
            'Host': 'www.anjuke.com',
        }
        # 注意这里的请求头我们在不同的情况下值是不一样的
        # 当然请求头你不换也许并不会导致出错，但是这也是一种反爬虫的方法，学习一下？
        url = get_url(city)
        #url = "https://www.anjuke.com/fangjia/xuzhou2018/jiuli/"
        get_ressponse(url=url,file = writer,headers=headers)
        # 将请求头传入
        # 传进链接和写对象
        t = uniform(1, 3)
        time.sleep(t)
        # 强制要求请求休息一下，我们这里用1，3之间的随机数
    except AttributeError:
        print('我发现了一个错误')
    except UnicodeEncodeError:
        print('有一个编码错误')
    # 两个错误检查

if __name__ == '__main__':
    with open('D:/testdata1/nanjing.csv', 'a', encoding='utf-8') as f:
        writer = csv.writer(f)
        for x in range(0,20):
            city = get_city()
            time.sleep(10)
            # 城市间的跳转等待时间稍微长一点，毕竟我们要更友好对不对！
            print('正在爬取的城市是：%s' % city)
            if city == None:
                break
            main(city)

