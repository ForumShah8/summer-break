import csv
filename = "data.csv"
alldata=[]
with open(filename,'r') as csvFile:
    Reader = csv.reader(csvFile)
    for row in Reader:
        if len(row) == 4:
            print(row)
        # print(len(row))