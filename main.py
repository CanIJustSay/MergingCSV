import csv

data1 = []
data2 = []

with open('dataset_1.csv') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        data1.append(row)

with open('dataset_2_sorted.csv') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        data2.append(row)

headers1 = data1[0]
headers2 = data2[0]
finalheaders = headers1 + headers2
planetdata1 = data1[1:]
planetdata2 = data2[1:]

finalplanetdata = []
for index, row in enumerate(planetdata1):
    finalplanetdata.append(planetdata1[index] + planetdata2[index])


with open ("bothDatas.csv","a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(finalheaders)
    csvwriter.writerows(finalplanetdata)