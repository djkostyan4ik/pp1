winter_semestr = {
    'math': 60,
    'programming': 30,
    'history': 15
}

result = 0
for key in winter_semestr:
    result += winter_semestr[key]

print('The total number of hours in the winter semester is',result)