import csv
# write nested list of dict to csv
import json

def nestedlist2csv(list, out_file):
    with open(out_file+".csv", 'w',encoding="utf-8") as f:
        w = csv.writer(f)
        fieldnames=list[0].keys()  # solve the problem to automatically write the header
        w.writerow(fieldnames)
        for row in list:
            w.writerow(row.values())

if __name__ == '__main__':
    with open("nj.json", 'r', encoding="utf-8") as load_f:
        data = json.load(load_f)
    nestedlist2csv(data, "nj")

