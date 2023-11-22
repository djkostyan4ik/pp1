array = [2, 3, 2, 5, 8, 1, 9, 8]
array2 = []
def unique_numbers(array):
    for i in array:
        if array.count(i) < 2:
            array2.append(i)
    return array2

unique_numbers(array)
print("Array: ", *array)
print("unique numbers: ", *array2)