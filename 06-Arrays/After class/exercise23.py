arr = [-15, 8, -31, 47, -2, 19]
min = arr[0]
max = arr[0]

for element in arr:
    if element <= min:
        min = element
    elif element >= max:
        max = element

print(max, min)