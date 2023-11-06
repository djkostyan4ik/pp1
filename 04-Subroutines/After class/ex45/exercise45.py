def f(expression):
    a = ''
    result = int(expression[0])
    for i in expression:
        if a == '+':
            result += int(i)
        elif a == '-':
            result -= int(i)
        a = i
    return result

if __name__=="__main__":
    print(f("2+3"))
    print(f("3+8+1"))
    print(f("2+3-4+5-0"))