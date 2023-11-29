import csv

with open('studentslist.txt',newline='') as f:
    r = csv.DictReader(f)
    for row in r:
        if int(row['age']) < 30:
            print(row['first_name'],row['last_name'],row['email'],sep='\t')