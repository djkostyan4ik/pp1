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






# def transpose_matrix(m):
#     arr = []
#     # the array is multidimensional
#     if type(m[0]) == type([0, 0, 0]):
#         for i in range(len(m[0])):
#             a = []
#             for j in range(len(m)):
#                 a.append(m[j][i])
#             arr.append(a)
#     # the array is onedimensional
#     if type(m[0]) == type(0):
#         for i in range(len(m)):
#             a = [m[i]]
#             arr.append(a)
#     return arr

arr1 = [[1,2,3],[4,5,6],[7,8,9]]
arr2 = [[1,2,3,4,5],[6,7,8,9,0]]
arr3 = [5,6,7,8]

print(my_arr(arr1))
print()
print(my_arr(transpose_matrix(arr1)))
print()
print("-----")
print()
print(my_arr(arr2))
print()
print(my_arr(transpose_matrix(arr2)))
print()
print("-----")
print()
print(*arr3)
print()
print(my_arr(transpose_matrix(arr3)))