import random

arr = []
for i in range(5):
    a = []
    for j in range(3):
        a.append(random.randint(0, 99))
    arr.append(a)

def my_arr(arr):

    max_array = []

    for row in range(len(arr)):
        max_array.append(max(arr[row]))
    max_max = len(str(max(max_array)))
    
    result = ''
    for row in range(len(arr)):
        for elem in range(len(arr[row])):
            result += str(arr[row][elem]).rjust(max_max)
            if elem != len(arr[row]) - 1:
                result += ' '
            else:
                result += '\n'
    return result


print(my_arr(arr))
print()

first_col = []
last_col = []
for row in arr:
    first_col.append(row[0])
    last_col.append(row[-1])

for row in arr:
    row[0] = last_col.pop(0)
    row[-1] = first_col.pop(0)

print(my_arr(arr))