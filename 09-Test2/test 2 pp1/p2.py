def f(y):
    years = 0
    if y == 1:
        years = 10
    elif y > 1:
        years = 10 + 10 +(y-2) * 4
    return years

if __name__ == '__main__':
    print(f(1))
    print(f(3))
    print(f(6))