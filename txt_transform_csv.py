#txt文件转csv
import csv

txt_file = "data/jiangsu_demo.txt"
csv_file = "data/jiangsu.csv"
in_txt = csv.reader(open(txt_file, "r",encoding="utf-8"), delimiter = ',',escapechar='\n')
out_csv = csv.writer(open(csv_file, 'w'))
out_csv.writerows(in_txt)