def f(binary_number):
    result = True
    for i in binary_number:
        if i != '1' and i != '0':
            result = False
    return result

if __name__ == '__main__':
    print(f('101101'))
    print(f('1311a10100'))