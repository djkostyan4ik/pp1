arr = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
]

for row in range(len(arr)):
    for elem in range(len(arr[0])):
        arr[row][elem] = (row + 1) * (elem + 1)

print(arr)

def my_arr(arr):

    max_array = []

    for row in range(len(arr)):
        max_array.append(max(arr[row]))
    max_max = len(str(max(arr[row])))

    result = ''

    for row in range(len(arr)):
        for elem in range(len(arr[row])):
            result += str(arr[row][elem]).rjust(max_max)
            if elem != len(arr[row])-1:
                result += ' '
            else:
                result += '\n'
    return result

print(my_arr(arr))