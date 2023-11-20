arr = [15, 8, 31, 47, 2, 19]
sum_of_all_elements = 0
length = len(arr)
result = ''
for element in arr:
    if element == arr[-1]:
        result += str(element)
    else:
        result += str(element) + " "
print(result)
for element in arr:
    sum_of_all_elements += element
    arithmetic_mean = sum_of_all_elements / length
print(arithmetic_mean)