# IP地址取自国内髙匿代理IP网站：http://www.xicidaili.com/nn/
# 仅仅爬取首页IP地址就足够一般使用
import urllib

from bs4 import BeautifulSoup
import requests
import random

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}

#从IP网站获取代理IP
def get_ip_list(url):
    web_data = requests.get(url=url,headers=headers)
    soup = BeautifulSoup(web_data.text, 'lxml')
    ips = soup.find_all('tr')
    ip_list = []
    for i in range(1, len(ips)):
        ip_info = ips[i]
        tds = ip_info.find_all('td')
        ip_list.append(tds[1].text + ':' + tds[2].text)
    #检测ip可用性，移除不可用ip
    for ip in ip_list:
        try:
            proxy_host = "http://" + ip
            print(proxy_host)
            proxy_temp = {"http": proxy_host}
            url = "http://www.baidu.com"
            response = requests.get(url,proxies=proxy_temp,timeout=5)
        except Exception as e:
            ip_list.remove(ip)
            continue
    return ip_list

#从ip池中随机获取ip列表
def get_random_ip(ip_list):
    proxy_list = []
    #print(ip_list)
    for ip in ip_list:
        proxy_list.append('http://' + ip)
    proxy_ip = random.choice(proxy_list)
    proxies = {'http': proxy_ip}
    return proxies

if __name__ == '__main__':
    url = 'http://www.xicidaili.com/nn/'
    ip_list = get_ip_list(url)
    with open('data/ip.txt','w',encoding='utf-8') as f:
        #print(ip_list)
        for line in ip_list:
            f.writelines(line+",")
    # proxies = get_random_ip(ip_list)
    # print(proxies)


