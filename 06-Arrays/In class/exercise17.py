arr = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

n = 0
for row in arr:
    arr[arr.index(row)][n] = 1
    n += 1
for row in arr:
    for elem in row:
        print(f'{elem}', end = ' ')
    print()