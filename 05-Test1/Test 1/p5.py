def f(a,b):
    result = ''
    for i in range(a,b + 1):
        if int(i) % 2 == 0:
            result += str(i) + ','
    return result[:-1]


if __name__ == '__main__':
    print(f(2,3))
    print(f(3,11))
    print(f(4,6))