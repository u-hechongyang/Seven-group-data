#txt文件转csv
import csv

txt_file = "data/m_demo.txt"
csv_file = "data/"+"house_demo"+".csv"
#csv_file = "data/"+"chendu"+"_"+"street"+".csv"
in_txt = csv.reader(open(txt_file, "r",encoding="utf-8"), delimiter = ',')
out_csv = csv.writer(open(csv_file, 'w'))
out_csv.writerows(in_txt)