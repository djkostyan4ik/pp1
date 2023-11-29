import random 

arr = []
for row in range(4):
    a = []
    for elem in range(2):
        a.append(random.randint(0,99))
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
            if elem != len(arr[row])-1:
                result += ' '
            else:
                result += '\n'
    return result

print(arr)
print(my_arr(arr))