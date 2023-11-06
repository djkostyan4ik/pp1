def f(detector):
    people = 0
    result = False
    for i in detector:
        if i == '+':
            people += 1
        elif i == '-':
            people -= 1
        if people >= 3:
            result = True
    return result

if __name__ == '__main__':
    print(f('+-+++-+---'))
    print(f('+-+-+-+-'))
    print(f('+-++-+--'))
    print(f('+-++-++-+---'))