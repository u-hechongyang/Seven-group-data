#-*-coding:utf-8 -*-
import re

fi = open("data/m.txt","r",encoding="utf-8")
fo = open("data/m_demo.txt", "a",encoding="utf-8")
for line in fi:
    if line == '\n':
        line = line.strip("\n")
    ls = line.split(',')
    if "其他" in ls[1] or "其他" in ls[2]:
        continue
    if "其它" in ls[1] or "其它" in ls[2]:
        continue
    if "周边" in ls[1] or "周边" in ls[2]:
        continue
    date = str(ls[3])
    lls = date.split('/')
    year = int(lls[0])
    month = int(lls[1])
    if year >=2018:
        line = ls[0] + "," + ls[1] + "," + ls[2] + "," + lls[0] + "," + lls[1] + "," + ls[4]
        fo.write(line)

fi.close()
fo.close()