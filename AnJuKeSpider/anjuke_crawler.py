import requests
from concurrent.futures import ThreadPoolExecutor
from pyquery import PyQuery as pq
import threading
import csv
from random import uniform,choice
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

#获得各个街道
def get_street_page_url(municipal_url):
    street_list_url = list()
    headers =  {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    }
    try:
        response = requests.get(municipal_url, headers=headers)
        # print(response.status_code, response.text)
        doc = pq(response.text)
        lis = doc('.sub-items a').items()
        for a in lis:
            street_list_url.append(a.attr('href'))
        #测试获得的street_url是否正确
        #print(street_list_url)
        return street_list_url
    except:
        print("获取各个区的链接出错")
        return None

#解析各个街道的内容
def detail_street_parser(res):
    global city
    detail_urls = res.result()
    if not detail_urls:
        print("detail url 为空")
        return None
    headers =  {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Referer': 'https://www.anjuke.com/fangjia/'
    }
    for detail_url in detail_urls:
        try:
            html = requests.get(url=detail_url, headers=headers,timeout=3)
            Soup = BeautifulSoup(html.text, 'lxml')
            house_list = Soup.find_all(name='div', attrs={'class': 'fjlist-box boxstyle2'})
            house_demo = Soup.find_all(name='span', attrs={'class': 'selected-item'})

            hdemo01 = house_demo[0].get_text()
            hdemo02 = house_demo[1].get_text()
            for ul in house_list:
                for li in ul.find_all(name="li"):
                    house_date = li.b.string
                    year = house_date[0:house_date.index("年")]
                    month = house_date[house_date.index("年")+1:house_date.index("月")]
                    house_date = year+"/"+month
                    house_price = li.span.string
                    house_price = house_price[0:house_price.index("元")]
                    #打印输入到文件中解析的内容是否正确
                    print(city+","+hdemo01+","+hdemo02+","+house_date+","+house_price)
                    writer.writerow([city, hdemo01, hdemo02, house_date, house_price])

                break
        except:
            print("获取详情页出错,换ip重试")
            # 代理服务器
            proxyHost = "http-dyn.abuyun.com"
            proxyPort = "9020"

            # 代理隧道验证信息
            proxyUser = "HSZ7ZZ4WI9AIK41D"
            proxyPass = "C70238B553C82C9D"

            proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
                "host": proxyHost,
                "port": proxyPort,
                "user": proxyUser,
                "pass": proxyPass,
            }

            proxy_handler = {
                "http": proxyMeta,
                "https": proxyMeta,
            }
            # proxies = {
            #     #"http": "http://" + get_valid_ip(),
            #     "http": "http://207.246.110.67:25565",
            # }
            try:
                html = requests.get(url=detail_url, headers=headers, proxies=proxy_handler)
                Soup = BeautifulSoup(html.text, 'lxml')
                house_list = Soup.find_all(name='div', attrs={'class': 'fjlist-box boxstyle2'})
                house_demo = Soup.find_all(name='span', attrs={'class': 'selected-item'})

                hdemo01 = house_demo[0].get_text()
                hdemo02 = house_demo[1].get_text()
                for ul in house_list:
                    for li in ul.find_all(name="li"):
                        house_date = li.b.string
                        year = house_date[0:house_date.index("年")]
                        month = house_date[house_date.index("年") + 1:house_date.index("月")]
                        house_date = year + "/" + month
                        house_price = li.span.string
                        # 打印输入到文件中解析的内容是否正确
                        print(city+","+hdemo01 + "," + hdemo02 + "," + house_date + "," + house_price)
                        writer.writerow([city,hdemo01,hdemo02,house_date,house_price])
                        #print(detail_dict)
                    break
            except:
                print("重试失败...")

def main():
    global city
    # cq,cs,nj,dl,wh,cc
    city_list = ['foshan','guangzhou','huizhou','shenzhen','zhanjiang','zh']
    for city in city_list:
        time.sleep(3)
        for index in range(2012, 2020):
            time.sleep(3)
            municipal_list = get_municipal_page_url(city, index)  # index

            p = ThreadPoolExecutor(1)

            for municipal_url in municipal_list:
                p.submit(get_street_page_url, municipal_url).add_done_callback(detail_street_parser)
                # 这里的回调函数拿到的是一个对象。
                # 先把返回的res得到一个结果。即在前面加上一个res.result(),这个结果就是get_detail_page_url的返回

    p.shutdown()

if __name__ == '__main__':
    with open('data/guangzhou.csv','w',encoding="utf-8") as f:
        writer = csv.writer(f,delimiter=",")
        main()