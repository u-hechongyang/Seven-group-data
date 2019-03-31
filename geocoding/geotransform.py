import json
from urllib.request import urlopen, quote
import requests,csv
'''
调用百度地图接口实现地理位置向经纬度的转换
'''

def getlnglat(address):
    url = 'http://api.map.baidu.com/geocoder/v2/'
    output = 'json'
    ak = 'Nz4Cim79NepkCtXjuZb24WormpZKPtCI'
    add = quote(address) #由于本文城市变量为中文，为防止乱码，先用quote进行编码
    uri = url + '?' + 'address=' + add  + '&output=' + output + '&ak=' + ak
    req = urlopen(uri)
    res = req.read().decode() #将其他编码的字符串解码成unicode
    temp = json.loads(res) #对json数据进行解析
    return temp

with open(r'data/one_transform.csv','a',encoding="utf-8") as f: #建立json数据文件
    w = csv.writer(f)
    w.writerow(['areaName','longitude','latitude','year','month','unitPrice'])
    with open(r'data/un_nj.csv', 'r',encoding="utf-8") as csvfile: #打开csv
        reader = csv.reader(csvfile)
        for line in reader: #读取csv里的数据
            # 忽略第一行
            if reader.line_num == 1: #由于第一行为变量名称，故忽略掉
                continue
                # line是个list，取得所有需要的值
            if line:
                b = line[0].strip()+line[1].strip()+line[2].strip()  # 将第一列city读取出来并清除不需要字符
                lng = getlnglat(b)['result']['location']['lng']  # 采用构造的函数来获取经度
                lat = getlnglat(b)['result']['location']['lat']  # 获取纬度
                lng = float(lng)
                lat = float(lat)
                year = int(line[3])
                month = int(line[4])
                price = float(line[5])
                w.writerow([b,lng, lat,year,month,price])

