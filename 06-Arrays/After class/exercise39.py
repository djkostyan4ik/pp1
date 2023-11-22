array = [1, 2, 3, 4, 5, 6, 7, 8]
even_result = []
odd_result = []
for element in array:
    if element % 2 == 0:
        even_result.append(element)
    else:
        odd_result.append(element)
whole_result = even_result + odd_result
print(whole_result)
