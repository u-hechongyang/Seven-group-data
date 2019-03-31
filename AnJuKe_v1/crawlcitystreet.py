# _*_ coding:utf-8 _*_
import time,csv
from random import uniform,choice
import requests
from bs4 import BeautifulSoup

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
cities = ['binhushijicheng','binhujiaris','baohegongyeyuan','dongchengang','dazhonglou','gaosushidaiguangchang','gaotienanzhan','gedadian','huanhucbd','hejiafugouwujie','linhus','luogangjichang','nanqizhongtiesiju','nanxunmenqiao','nanmenhuanchengzhongxin','sishiliuzhonga','shouchunzhongxuea','weiganga','wulimiao','xinshengfu','yungulu','zhougudui',
'beimenb','bantang','chunhuixuexiao','chaohulinhu','chaohuzhoubianh','dongmenh','guishan','nanmenh','ximenh',
'daishanhu','feidongxincheng','feitongxiancheng',
'feixixiancheng','feixizhoubian','guanting','zipengshan',
'lujiangb',
'beiyihuan','bozhoulu','baishuiba','dayangzhen','haitangshequ','linghu','luyangzhoubian','silihe','sanxiaokou','sipailoua','shuangganga','shuangfengluyanggongyeyuan','sanshigang','xinglinhuayuan',
'anhuidashichangw','huochezhanw','hepingguangchang','huachonggongyuan','heyulu','lieshanlu','longgangb','qilitangw','qichezhan','shaoquanhu','shengtaigongyuanw','sanlijie','shuguangyingyuan','taochonghu','xinanjianglu','yaohaigongyuanw','yaohaiwanda','yufenghuashi','zhijiaocheng',
'anhuidaxue','boyankejiyuan','daxuechengw','dashushanw','furonglu','fenghuangchenghf','fangxingdadao','guichilu','hefeibazhong','huangqianwang','keyunxizhanhf','lianhualu','mingzhuguangchangw','nanyanhuw','nanqili','qingyangbeilu','roulianchang','shuxihu','sanlian','shushanchanyeyuan','shizhengwubangongqu','tianehuw','xiangzhuangdadao','zhiwuyuanw',
'akuiliya','beichengzhonghuancheng','beichengshijicheng','changfengzhoubian','gangji']


# 一个我们将要爬取城市的列表
#'xiaoshia',
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

def get_url(index,city):
    if city == None:
        return
    # 城市值为None时，我们就跳出
    else:
        url = 'https://www.anjuke.com/fangjia/hf{index}/{city}/'.format(index=index,city=city)
        return url

def get_ressponse(url,file,headers,index):
    try:
        html = requests.get(url=url,headers=headers,verify=False)
    except Exception:
        print("异常"+city)
        time.sleep(10)
        html = requests.get(url=url, headers=headers, verify=False)
    Soup = BeautifulSoup(html.text,'lxml')
    house_list = Soup.find_all(name='div', attrs={'class': 'fjlist-box boxstyle2'})
    house_demo = Soup.find_all(name='span', attrs={'class':'selected-item'})
    #print(house_demo[0].get_text())
    #print(house_demo[1].get_text())
    try:
        hdemo01 = house_demo[0].get_text()
        hdemo02 = house_demo[1].get_text()
        for ul in house_list:
            for li in ul.find_all(name="li"):
                house_date = li.b.string
                house_price = li.span.string
                print(house_date)
                print(house_price)
                file.writerow([hdemo01, hdemo02, house_date, house_price])
            break
    except Exception:
        print("list index out of range")
        for ul in house_list:
            for li in ul.find_all(name="li"):
                house_date = li.b.string
                house_price = li.span.string
                print(house_date)
                print(house_price)
                file.writerow([house_date,house_price])
            break


def main(city):
    for index in range(2012, 2020):
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Referer': 'https://www.anjuke.com/fangjia/hf{index}/{city}/'.format(index=index,city=city),
                'Host': 'www.anjuke.com'.format(city=city),
                'Connection': 'close',
            }
            # 注意这里的请求头我们在不同的情况下值是不一样的
            # 当然请求头你不换也许并不会导致出错，但是这也是一种反爬虫的方法，学习一下？
            url = get_url(index,city)
            get_ressponse(url=url, file=writer,headers=headers,index = index)
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
    with open('D:/testdata/hf_street.csv','a',encoding='utf-8') as f:
        # 因为默认的读写操作是gbk，所以最好还是改成utf-8
        # 在这里打开文件而不是在循环中打开，我们就可以避免频繁的IO操作
        writer = csv.writer(f)
        # 创建一个写对象
        #writer.writerow(['house_date,house_price'])
        # 写入表头 x为城市个数
        for x in range(0,1000):
            city = get_city()
            time.sleep(10)
            # 城市间的跳转等待时间稍微长一点，毕竟我们要更友好对不对！
            print('正在爬取的城市是：%s' % city)
            if city == None:
                break
                # 如果没有城市了，那就跳出循环停止了。
            #writer.writerow([city])
            main(city)
