def f(e):
    result = eval(e)
    return result

if __name__ == '__main__':
    print(f('2+3'))
    print(f('3+8+1'))
    print(f('2+3-4+5-0'))