import random 
array = []
for i in range(0,7):
    x = random.randint(0,999)
    array.append(x)
y = random.randint(100,999)
array.append(y)

result = ''
print('-' * 41)
for elem in array:
    if elem == array[-1]:
        result += '| ' + str(elem) + '|'
    elif len(str(elem)) == 3:
        result += '| '+ str(elem)
    elif len(str(elem)) == 2:
        result += '|  ' + str(elem)
    elif len(str(elem)) == 1:
        result += '|   ' + str(elem)
print(result)
print('-' * 41)