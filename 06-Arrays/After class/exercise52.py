import random

def display_arr(array):

    # find how long are numbers in the array
    max_array = []

    for i in range(len(array)):
        max_array.append(max(array[i]))
    
    max_max = len(str(max(max_array)))

    # prepare string for displaying the array
    x = ""

    for i in range(len(array)):
        for j in range(len(array[i])):
            x += str(arr[i][j]).rjust(max_max)
            if j != len(array[i]) - 1:
                x += " "
            else:
                x += "\n"

    return x

arr = []
for i in range(5):
    a = []
    for j in range(3):
        a.append(random.randint(0, 99))
    arr.append(a)


print(display_arr(arr))
print()
print(arr)
first_col = []
last_col = []
for i in arr:
    first_col.append(i[0])
    last_col.append(i[-1])

for i in arr:
    i[0] = last_col.pop(0)
    i[-1] = first_col.pop(0)

print(display_arr(arr))