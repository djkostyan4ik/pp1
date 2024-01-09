def f(d):
    people = 0
    for sign in d:
        if sign == '+':
            people += 1
        elif sign == '-':
            people -= 1
    return people

if __name__ == '__main__':
    print(f('+-+++-+---'))
    print(f('+-+++++-'))
    print(f('+-++-++-+'))