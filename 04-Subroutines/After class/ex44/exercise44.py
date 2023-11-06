def f(password):
    a = ''
    length = len(password)
    for i in password:
        if i == a:
            return False
        a = i
        if i != a:
            return True
    if length >= 6:
        return True
    else:
        return False
    

if __name__ == '__main__':
    print(f('ax15'))
    print(f("book123"))
    print(f("A2water3"))
    print(f("qwerty"))
    print(f(''))