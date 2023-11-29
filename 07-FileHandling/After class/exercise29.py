import re


with open('grades.txt') as file:
    text = file.read()
grades = re.findall("\\d.\\d",text)

sum = 0

for grade in grades:
    sum += float(grade)

grades.sort()

length = len(grades)

ar_mean = sum / length

print(round(ar_mean,2))