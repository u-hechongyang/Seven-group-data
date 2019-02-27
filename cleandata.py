#-*-coding:utf-8 -*-
import re

fi = open("data/jiangsu.txt","r",encoding="utf-8")
fo = open("data/jiangsu_demo.txt", "w+")
for line in fi:
    if line == '\n':
        line = line.strip("\n")
    results = re.findall('(\d+).*?(\d+).*?(\d+)',line,re.S)
    for result in results:
        line = result[0]+"-"+result[1]+","+result[2]+"\n"
    fo.write(line)

fi.close()
fo.close()