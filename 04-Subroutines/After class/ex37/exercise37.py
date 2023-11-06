def f(n):
    a = 0
    b = 1
    temp = 0

    if n > 2:
        for i in range(2, n):
            temp = b
            b += a
            a = temp
        return b
    elif n == 2:
        return b
    elif n == 1:
        return a
    
if __name__ == '__main__':
    print(f(5))
    print(f(9))