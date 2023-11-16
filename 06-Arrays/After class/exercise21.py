arr = [15, 8, 31, 47, 2, 19]
arr2 = arr.copy()
arr2 = arr2[::-1]
result = ''
result2 = ''
for element in arr:
    if element == arr[-1]:
        result += str(element)
    else:
        result += str(element) + " "

for element in arr2:
    if element == arr2[-1]:
        result2 += str(element)
    else:
        result2 += str(element) + " "

        
print('existed array: ', result)
print('reverse array: ', result2)