import csv
from flask import Flask, request, jsonify
alldata = []
def parserFunction(file):
    if len(alldata)>0:
        alldata.clear()
    with open(file,'r') as csvFile:
        Reader = csv.reader(csvFile)
        for row in Reader:
            row = [element.strip() for element in row]
            if len(row) == 4:
                alldata.append(row)
    return alldata

app = Flask(__name__)
@app.route('/transactions',methods=['POST'])
def storeData():
    csvFile = request.files['data']
    if csvFile:
        fileName = csvFile.filename
        csvFile.save(fileName)
        jsonData = parserFunction(fileName)
    return jsonData,200

@app.route('/report',methods=['GET'])
def generateReport():
    print(alldata)
    grossRevenue = 0
    totalExpense = 0
    for items in alldata:
        print(items)
        if items[1] == 'Income':
            grossRevenue = grossRevenue + float(items[2])
        elif items[1] == 'Expense':
            totalExpense = totalExpense + float(items[2])
    finalreport = {
        "gross-revenue": grossRevenue,
        "expenses": totalExpense,
        "net-revenue": grossRevenue - totalExpense
    }
    return jsonify(finalreport),200
app.run()