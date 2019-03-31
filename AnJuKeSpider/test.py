import requests

from concurrent.futures import ThreadPoolExecutor

from pyquery import PyQuery as pq

import json

import threading
import csv
from random import uniform,choice
from bs4 import BeautifulSoup

import time

# html = '''
# <span class="elem-l">
#         <span class="selected-item">全部</span>
#         <a href="http://www.anjuke.com/fangjia/foshan2019/chanchengqu/">禅城</a>
#         <a href="http://www.anjuke.com/fangjia/foshan2019/shundequ/">顺德</a>
#         <a href="http://www.anjuke.com/fangjia/foshan2019/nanhaiqu/">南海</a>
#         <a href="http://www.anjuke.com/fangjia/foshan2019/gaomingqu/">高明</a>
#         <a href="http://www.anjuke.com/fangjia/foshan2019/sanshuiqu/">三水</a>
#         <!--            <a href="">江苏</a>-->
#         <!--			<a href="">浙江</a>-->
#         <!--			<a href="">湖南</a>-->
#         <!--			<a href="">广东</a>-->
#         <!--			<a href="">江西</a>-->
#         <!--			<a href="">福建</a>-->
# </span>
# '''

# doc = pq(html)
# page_url_list = list()
# lis = doc('.elem-l a').items()
# for a in lis:
#     page_url_list.append(a.attr('href'))
# print(page_url_list)

# html = '''
# <div class="sub-items">
#         <span class="selected-item">全部</span>
#         <span class="sub-letter-item">c</span>
#         <a href="http://www.anjuke.com/fangjia/foshan2019/chaoanb/">朝安</a>
#         <span class="sub-letter-item">d</span>
#         <a href="http://www.anjuke.com/fangjia/foshan2019/dongpingxincheng/">东平新城</a>
#         <span class="sub-letter-item">f</span>
#         <a href="http://www.anjuke.com/fangjia/foshan2019/fenjiangbei/">汾江北</a>
#         <a href="http://www.anjuke.com/fangjia/foshan2019/foping/">佛平</a>
#         <span class="sub-letter-item">g</span>
#         <a href="http://www.anjuke.com/fangjia/foshan2019/gaoji/">高基</a>
#         <span class="sub-letter-item">h</span>
#         <a href="http://www.anjuke.com/fangjia/foshan2019/hujing/">湖景</a>
#         <span class="sub-letter-item">j</span>
#         <a href="http://www.anjuke.com/fangjia/foshan2019/jihuayuan/">季华园</a>
#         <a href="http://www.anjuke.com/fangjia/foshan2019/jihualiulu/">季华六路</a>
#         <span class="sub-letter-item">k</span>
#         <a href="http://www.anjuke.com/fangjia/foshan2019/kuiqi/">魁奇</a>
#         <span class="sub-letter-item">l</span>
#         <a href="http://www.anjuke.com/fangjia/foshan2019/lvjing/">绿景</a>
#         <a href="http://www.anjuke.com/fangjia/foshan2019/lianda/">莲大</a>
#         <span class="sub-letter-item">n</span>
#         <a href="http://www.anjuke.com/fangjia/foshan2019/nanzhuang/">南庄</a>
#         <span class="sub-letter-item">p</span>
#         <a href="http://www.anjuke.com/fangjia/foshan2019/pujun/">普君</a>
#         <span class="sub-letter-item">s</span>
#         <a href="http://www.anjuke.com/fangjia/foshan2019/shiwan/">石湾</a>
#         <span class="sub-letter-item">t</span>
#         <a href="http://www.anjuke.com/fangjia/foshan2019/tongjifs/">同济</a>
#         <span class="sub-letter-item">w</span>
#         <a href="http://www.anjuke.com/fangjia/foshan2019/wufengfs/">五峰</a>
#         <span class="sub-letter-item">z</span>
#         <a href="http://www.anjuke.com/fangjia/foshan2019/zhangcha/">张槎</a>
#         <a href="http://www.anjuke.com/fangjia/foshan2019/zumiao/">祖庙</a>
# </div>
# '''
# doc = pq(html)
# page_url_list = list()
# lis = doc('.sub-items a').items()
# for a in lis:
#     page_url_list.append(a.attr('href'))
# print(page_url_list)

