arr = [15, 8, 31, 47, 2, 19]
# print(' '.join(str(element) for element in arr))
print(' '.join(map(str,arr)))
whole_sum = 0
amount = 0
while amount < len(arr):
    whole_sum += arr[amount]
    amount += 1
mean = whole_sum / amount
print(mean)

