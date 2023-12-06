import json

with open('euro.json') as file:
    data = json.load(file)

rates = data['rates']

heading = 'Data\t\tBuying Rate\tSelling Rate\n============================================'

print(heading)

for i in rates:
    print(f'{i['effectiveDate']:10} {i['bid']:11} {i['ask']:15}')