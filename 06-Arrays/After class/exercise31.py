array = [2, 3, 2, 5, 8, 1, 9, 8]
def unique_numbers(array):
    return [i for i in array if array.count(i) < 2]

unique_numbers(array)
print("Array: ", *array)
array2 = unique_numbers(array) 
print("unique numbers: ", *array2)