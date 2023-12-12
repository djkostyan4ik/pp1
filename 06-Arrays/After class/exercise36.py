my_tuple = (50,20,40,50,30,50)
def occurences(value, my_tuple):
    count = 0
    for element in my_tuple:
        if value == element:
            count += 1
    return count

if __name__ == '__main__':
    print("Tuple:",','.join(map(str,my_tuple)))
    print("Value:",50)
    print("Number of occurences:",occurences(50,my_tuple))