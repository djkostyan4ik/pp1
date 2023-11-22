def second_largest_element(array):
    array = sorted(array)
    return array[-2]

def my_difference(array):
    array = sorted(array)
    return array[-1]-array[0]

def my_median(array):
    array = sorted(array)
    middle = len(array) // 2
    return (array[middle] + array[-middle-1]) / 2

def my_array(array):
    array = sorted(array)
    array2 = []
    array2.append(array[0])
    array2.append(array[-1])
    return array2

def separated(array):
        return (array)