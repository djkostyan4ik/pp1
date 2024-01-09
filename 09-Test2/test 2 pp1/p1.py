def f(n):
    if n > 1 and n % 2 != 0 and n % 3 != 0 :
        return True
    else:
        return False

if __name__ == '__main__':
    print(f(1))
    print(f(7))
    print(f(30))
    print(f(5))
    print(f(121))
    print(f(144))