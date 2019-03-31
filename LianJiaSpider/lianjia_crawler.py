# -*- coding: utf-8 -*-

import requests

from concurrent.futures import ThreadPoolExecutor

from pyquery import PyQuery as pq

import json

import threading


import time


def get_list_page_url(city):

    start_url = "https://{}.lianjia.com/ershoufang".format(city)
    headers =  {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    }
    try:
        response = requests.get(start_url, headers=headers)
        # print(response.status_code, response.text)
        doc = pq(response.text)
        total_num =  int(doc(".resultDes .total span").text())
        total_page = total_num // 30 + 1
        # 只能访问到前一百页
        if total_page > 100:
            total_page = 100

        page_url_list = list()

        for i in range(total_page):
            url = start_url + "/pg" + str(i + 1) + "/"
            page_url_list.append(url)
            #print(url)
        return page_url_list

    except:
        print("获取总套数出错,请确认起始URL是否正确")
        return None


detail_list = list()

# 需要先在本地开启代理池
# 代理池仓库: https://github.com/Python3WebSpider/ProxyPool
def get_valid_ip():
    url = "http://localhost:5000/get"
    try:
        ip = requests.get(url).text
        return ip
    except:
        print("请先运行代理池")


def get_detail_page_url(page_url):
    global detail_list
    headers =  {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Referer': 'https://bj.lianjia.com/ershoufang'
    }

    try:
        response = requests.get(page_url,headers=headers,timeout=3)
        doc = pq(response.text)
        i = 0
        detail_urls = list()
        #调用items()方法实现对每一个li节点进行遍历
        for item in doc(".sellListContent li").items():
            i += 1
            if i == 31:
                break
            child_item = item(".noresultRecommend")
            if child_item == None:
                i -= 1
            detail_url = child_item.attr("href")
            detail_urls.append(detail_url)
        return detail_urls
    except:
        print("获取列表页" + page_url + "出错")

lock = threading.Lock()

def detail_page_parser(res):
    global detail_list
    detail_urls = res.result()
    if not detail_urls:
        print("detail url 为空")
        return None
    headers =  {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Referer': 'https://bj.lianjia.com/ershoufang'
    }
    for detail_url in detail_urls:
        try:
            response = requests.get(url=detail_url, headers=headers,timeout=3)
            #print(response.status_code)
            detail_dict = dict()
            doc = pq(response.text)

            area_name = doc(".areaName .info a").eq(0).text().strip()
            unit_price = doc(".unitPriceValue").text()
            unit_price = float(unit_price[0:unit_price.index("元")])
            total_price = float(doc(".price .total").text())
            floor_area = doc(".area .mainInfo").text()
            floor_area = float(floor_area[0:floor_area.index("平米")])

            list_content = list()
            lis = doc('.base .content li')
            for li in lis.items():
                li.find('span').remove()
                list_content.append(li.text())
            #print(list_content)

            houses = list_content[0]
            rooms = int(houses[0:houses.index("室")])
            halls = int(houses[houses.index("室") + 1:houses.index("厅")])
            floors = list_content[1]
            floors = floors[:floors.index("层")]
            house_struct = list_content[3]
            # floor_area = list_content[4]
            # floor_area = float(floor_area[0:floor_area.index("㎡")])
            directions = list_content[6]
            decoration = list_content[8]
            elevator_porporation = list_content[9]
            iselevator = list_content[10]
            property_year = list_content[11]
            property_year = int(property_year[0:property_year.index("年")])

            detail_dict["areaName"] = area_name
            detail_dict["unitPrice"] = unit_price
            detail_dict["rooms"] = rooms
            detail_dict["halls"] = halls
            detail_dict["floors"] = floors
            detail_dict["houseStruct"] = house_struct
            detail_dict['floorArea'] = floor_area
            detail_dict['directions'] = directions
            detail_dict['decoration'] = decoration
            detail_dict['elevaPropora'] = elevator_porporation
            detail_dict['isElevator'] = iselevator
            detail_dict['yearProperty'] = property_year
            detail_dict["totalPrice"] = total_price

            detail_list.append(detail_dict)


            print(area_name," ", unit_price, " ",rooms, " ", halls, " ",floors," ",house_struct, " ", floor_area, " ", directions, " ", decoration, " ",
                  elevator_porporation, " ", iselevator, " ", property_year, " ",total_price)

        except:
            print("获取详情页出错,换ip重试")
            proxies = {
                "http": "http://" + get_valid_ip(),
            }
            try:
                response = requests.get(url=detail_url, headers=headers, proxies=proxies)
                #print(response.status_code)
                detail_dict = dict()
                doc = pq(response.text)
                area_name = doc(".areaName .info a").eq(0).text().strip()
                unit_price = doc(".unitPriceValue").text()
                unit_price = float(unit_price[0:unit_price.index("元")])
                floor_area = doc(".area .mainInfo").text()
                floor_area = float(floor_area[0:floor_area.index("平米")])
                total_price = float(doc(".price .total").text())
                list_content = list()
                lis = doc('.base .content li')
                for li in lis.items():
                    li.find('span').remove()
                    list_content.append(li.text())
                print(list_content)

                houses = list_content[0]
                rooms = int(houses[0:houses.index("室")])
                halls = int(houses[houses.index("室") + 1:houses.index("厅")])
                floors = list_content[1]
                floors = floors[:floors.index("层")]
                house_struct = list_content[3]
                # floor_area = list_content[4]
                # floor_area = float(floor_area[0:floor_area.index("㎡")])
                directions = list_content[6]
                decoration = list_content[8]
                elevator_porporation = list_content[9]
                iselevator = list_content[10]
                property_year = list_content[11]
                property_year = int(property_year[0:property_year.index("年")])

                # 已下架的还会爬取，但是没有价格
                if unit_price>0:
                    detail_dict["areaName"] = area_name
                    detail_dict["unitPrice"] = unit_price
                    detail_dict["rooms"] = rooms
                    detail_dict["halls"] = halls
                    detail_dict["floors"] = floors
                    detail_dict["houseStruct"] = house_struct
                    detail_dict['floorArea'] = floor_area
                    detail_dict['directions'] = directions
                    detail_dict['decoration'] = decoration
                    detail_dict['elevaPropora'] = elevator_porporation
                    detail_dict['isElevator'] = iselevator
                    detail_dict['yearProperty'] = property_year
                    detail_dict["totalPrice"] = total_price

                    print(area_name, " ", unit_price, " ", rooms, " ", halls, " ", floors, " ", house_struct, " ",floor_area, " ", directions, " ", decoration, " ",
                          elevator_porporation, " ", iselevator, " ", property_year, " ", total_price)
            except:
                print("重试失败...")


def save_data(data,filename):
    with open(filename+".json", 'w', encoding="utf-8") as f:
        f.write(json.dumps(data, indent=2, ensure_ascii=False))

def main():
    # cq,cs,nj,dl,wh,cc
    city_list = ['nj']
    for city in city_list:
        page_url_list = get_list_page_url(city)

        p = ThreadPoolExecutor(30)

        for page_url in page_url_list:
            p.submit(get_detail_page_url, page_url).add_done_callback(detail_page_parser)
        # 这里的回调函数拿到的是一个对象。
        # 先把返回的res得到一个结果。即在前面加上一个res.result(),这个结果就是get_detail_page_url的返回
        p.shutdown()

        print(detail_list)

        save_data(detail_list, city)

        detail_list.clear()

if __name__ == '__main__':
    old = time.time()
    main()
    new  = time.time()
    delta_time = new - old
    print("程序共运行{}s".format(delta_time))








