def f(c):
    result = 0
    imp_val = ['A', 'K', 'Q', 'J', 'T']
    for sign in c:
        if sign in imp_val:
            result += 10
        else:
            result += int(sign)
    return str(result)

if __name__ == '__main__':
    print(f('2K9'))
    print(f('234AJ7'))