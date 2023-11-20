arr = [8, 2, 5, 1, 9]
result = ''
result2 = ''
for element in arr:
    if element == arr[-1]:
        result += str(element)
    else:
        result += str(element) + " "
print("Array", result)
arr2 = arr.copy()
for element in arr2:
    if element == arr2[-1]:
        element = element ** 2
        result2 += str(element)
    else:
        element = element ** 2
        result2 += str(element) + " "
print("Second power: ", result2)