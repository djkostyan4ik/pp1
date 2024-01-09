def f(w):
    result = ''
    position = 1
    for i in w:
        position += 1
        if position % 2 == 0:
            result += str(i) + '+'
        else:
            result += str(i) + '-'

    return result[:-1]

if __name__ == '__main__':
    print(f('abcdefgh'))
    print(f('xyz'))
    print(f('k'))
    print(f(''))
