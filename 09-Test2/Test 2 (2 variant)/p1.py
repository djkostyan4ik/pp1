def f(n):
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a + b
        if n == b:
            return True
    return False

if __name__ == '__main__':
    print(f(2))