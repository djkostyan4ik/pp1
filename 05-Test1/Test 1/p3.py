def f(p):
    a = ''
    length = len(p)
    istrue = True
    for i in p:
        if i == a:
            istrue = False
            return False
        a = i
    if length >= 6:
        return True
    else:
        return False

if __name__== '__main__':
    print(f('ax15'))
    print(f('book123'))
    print(f('A2water'))
    print(f('qwerty'))
    print(f(''))