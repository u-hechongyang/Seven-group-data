import requests
from pyquery import PyQuery as pq
import threading
import csv
from bs4 import BeautifulSoup
import time

lock = threading.Lock()
city = ''

import random
def get_valid_ip():
    ip_list = list()
    try:
        with open('data/ip.txt','r',encoding='utf-8') as f:
            content = f.read()
            ip_list = content.split(',')
        #print(ip_list)
        proxy_ip = random.choice(ip_list)
        return proxy_ip
    except:
        print("请先运行代理池")

#获得各个区的url
def get_municipal_page_url(city,index):
    start_url = 'https://www.anjuke.com/fangjia/{city}{index}/'.format(index=index,city=city)
    headers =  {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    }
    try:
        response = requests.get(start_url, headers=headers)
        # print(response.status_code, response.text)
        doc = pq(response.text)
        municipal_url_list = list()
        lis = doc('.elem-l a').items()
        for a in lis:
            municipal_url_list.append(a.attr('href'))
        #测试 获取链接是否出错 print(municipal_url_list)
        return municipal_url_list
    except:
        print("获取各个区的链接出错")
        return None

#解析各个街道的内容
def detail_muncipal_parser(municipal_url):
    headers =  {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Referer': 'https://www.anjuke.com/fangjia/'
    }
    html = requests.get(url=municipal_url, headers=headers, timeout = 3)
    Soup = BeautifulSoup(html.text, 'lxml')
    house_list = Soup.find_all(name='div', attrs={'class': 'fjlist-box boxstyle2'})
    house_demo = Soup.find_all(name='span', attrs={'class': 'selected-item'})
    try:
        for ul in house_list:
            for li in ul.find_all(name="li"):
                house_date = li.b.string
                year = house_date[0:house_date.index("年")]
                month = house_date[house_date.index("年") + 1:house_date.index("月")]
                house_date = year + "/" + month
                house_price = li.span.string
                house_price = house_price[0:house_price.index("元")]
                # 打印输入到文件中解析的内容是否正确
                print(city + "," + house_demo[0].get_text() + "," + house_date + "," + house_price)
                writer.writerow([city, house_demo[0].get_text(), house_date, house_price])
            break
    except Exception:
        print("index out of range")

def main():
    global city
    # cq,cs,nj,dl,wh,cc
    city_list = ['tianjin']
    #宁夏 yinchuan 山西 ty 陕西 xianyang 四川 chengdu 云南 km
    for city in city_list:
        time.sleep(3)
        for index in range(2012, 2020):
            municipal_list = get_municipal_page_url(city, index)  # index

            #p = ThreadPoolExecutor(0)

            for municipal_url in municipal_list:
                detail_muncipal_parser(municipal_url)


    #p.shutdown()

if __name__ == '__main__':
    with open('data/tianjin_muncipal.csv','w',encoding="utf-8") as f:
        writer = csv.writer(f,delimiter=",")
        main()