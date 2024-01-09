def f(d,v):
    count = 0
    values = d.values()
    for i in values:
        if v != i:
            count += 1
    return count

if __name__ == '__main__':
    print(f({'a': True, 'b': False, 'c': True, 'd': True,'e': True}, True))
    print(f({'a': True, 'b': False, 'c': True, 'd': True, 'e': True}, False))