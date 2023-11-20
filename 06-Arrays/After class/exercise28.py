def compare(array1, array2):
    if len(array1) != len(array2):
        return False
    for i in range(0, len(array1)):
        if array1[i] != array2[i]:
            return False
    return True




if __name__ == '__main__':
    # a
    array1 = ["water", "book", "sky"]
    array2 = ["water", "book", "sky"]
    # b
    # array1 = [True, False]
    # array2 = [True, False, True]
    # c
    # array1 = [5, 3, 1]
    # array2 = [5, 3, 1]
    # d
    # array1 = [3, 2, 1]
    # array2 = [3, 2]

print("Array: ", *array1)
print("Array2: ", *array2)
if (compare(array1, array2)):
    print("Comparison: arrays are the same")
else:
    print("Comparison: arrays are different")