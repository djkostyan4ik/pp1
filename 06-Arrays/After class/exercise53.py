def identity_matrix(n):
    arr = []
    for i in range(n):
        a = []
        for j in range(n):
            if i == j:
                a.append(1)
            else:
                a.append(0)
        arr.append(a)
    return arr

def my_array(arr):
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

print(my_array(identity_matrix(3)))
print()

print(my_array(identity_matrix(5)))
print()

print(my_array(identity_matrix(8)))
print()