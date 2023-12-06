import csv
import json

jsonArray = []

with open('products.csv') as csvfile:
    csvReader = csv.DictReader(csvfile)

    for row in csvReader:
        jsonArray.append(row)


with open('products.json','w') as jsonfile:
    jsonString = json.dumps(jsonArray,indent = 4)
    jsonfile.write(jsonString)


