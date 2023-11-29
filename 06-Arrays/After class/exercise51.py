import random 
arr = []
for row in range(5):
    a = []
    for elem in range(3):
        a.append(random.randint(0,99))
    arr.append(a)
print(arr)

first_row = arr[0]
last_row = arr[-1]
arr[0] = last_row
arr[-1] = first_row

print(arr)