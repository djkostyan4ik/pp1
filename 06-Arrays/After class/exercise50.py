arr = [
    [-38,19],
    [5,40],
    [-7,11],
    [29,16]
]

arr_min = arr[0][0]
min_row = 0
min_col = 0

arr_max = arr[0][0]
max_row = 0
max_col = 0

for row in range(len(arr)):
    for elem in range(len(arr[row])):
        if arr[row][elem] < arr_min:
            arr_min = arr[row][elem]
            min_row = row
            min_col = elem
        if arr[row][elem] > arr_max:
            arr_max = arr[row][elem]
            max_row = row
            max_col = elem

print(arr)
print(f"Min: {arr_min}\nRow: {min_row}\nColumn: {min_col}")
print(f"Max: {arr_max}\nRow: {max_row}\nColumn: {max_col}")