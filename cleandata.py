#-*-coding:utf-8 -*-
import re

fi = open("data/test02.txt","r",encoding="utf-8")
fo = open("data/test2_demo.txt", "w+")
for line in fi:
    if line == '\n':
        line = line.strip("\n")
    ls = line.split(',')
    results = re.findall('(\d+).*?(\d+).*?(\d+)',line,re.S)
    for result in results:
        line = ls[0]+","+ls[1]+","+result[0]+"-"+result[1]+","+result[2]+"\n"
    fo.write(line)

fi.close()
fo.close()