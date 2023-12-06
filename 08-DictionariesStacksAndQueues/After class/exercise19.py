import json


with open('students.json','r') as file:\
    info = json.load(file)

keys1 = ['name', 'surname', 'student ID']
keys2 = ['first_name', 'last_name', 'student_id']
result = []

for i in info:
    dictionary = {}
    for j in range(len(keys1)):
        dictionary[keys2[j]] = i[keys1[j]]
    result.append (dictionary)

with open('limited.json','w') as file2:
    json.dump(result,file2,indent = 4)
