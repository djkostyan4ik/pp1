def my_function(value, array):
    count = 0
    for number in array:
        if value < number:
            count += 1
    return count

if __name__ == '__main__':
    print(my_function(2, [3, 4, 1, 1, 5, 6]))