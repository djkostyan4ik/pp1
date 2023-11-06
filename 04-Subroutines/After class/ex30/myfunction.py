def f(number, even):
    result = 0
    if even == 'True':
        even == True
        for i in str(number):
            if int(i) % 2 == 0:
                result += int(i)
            else:
                continue
    else:
        even == False
        for i in str(number):
            if int(i) % 2 != 0:
                result += int(i)
            else:
                continue
    return result
