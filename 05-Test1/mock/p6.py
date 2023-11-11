def f(number, even):
    result = 0
    if even == True:
        for i in str(number):
            if  int(i) % 2 == 0:
                result += int(i)
    if even == False:
        for i in str(number):
            if int(i) % 2 != 0:
                result += int(i)

    return result

if __name__ == '__main__':
    print(f(3124, True))
    print(f(3124,False))
    print(f(20576,False))
    print(f(20576,True))
    print(f(13115,True))