arr = [
    [True, False],
    [True, True],
    [False, False]
]
print("Before: ", arr)
for row in arr:
    if row == [True, False]:
        arr[arr.index(row)] = [False, True]
    else:
        for elem in row:
            if elem == True:
                row[row.index(elem)] = False
            else:
                row[row.index(elem)] = True
print("After:  ", arr)
#     for element in row:
#         if element == True:
#             arr[][] = False
#         elif element == False:
#             arr[][] = True

# print(arr)