arr = [
    [7,3,7,9,0],
    [2,9,0,1,5],
    [3,8,6,4,7],
    [8,7,1,1,5]
]

length = len(arr[0]) - 1
count = 0

for i in range(len(arr)):
    count += arr[i][length]

print(arr)
print(count)