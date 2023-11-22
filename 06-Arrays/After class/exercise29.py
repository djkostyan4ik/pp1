array1 = [4, 36, 12, 28, 9, 44, 5]
array2 = [5, 1, 36]
for element1 in range(0, len(array1)):
    for element2 in range(0, len(array2)):
        if (array1[element1] == array2[element2]):
            break
    
    if (array1[element1] != array2[element2]):
        print(array1[element1], end = ' ')
