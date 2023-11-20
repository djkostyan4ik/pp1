def bublesort(array):
    length = len(array)

    for element in range(length):
        swapped = False

        for j in range(0, length-element-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
        if (swapped == False):
            break

if __name__ == '__main__':
    array = [1, 4, 6, 2, 3, 8, 5]
    bublesort(array)
    print('Sorted array:', *array)