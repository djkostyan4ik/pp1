def f(a,b):
    if a > b:
        result = f'"{a}-{b}={a-b}"'
        return result
    else:
        result = f'"{a}+{b}={a+b}"'
        return result

if __name__ == '__main__':
    print(f(20,8))
    print(f(8,12))
    print(f(7,7))