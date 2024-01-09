def f(product_code):
    if len(product_code) != 4:
        return False
    summa = (int(product_code[0]) + int(product_code[1]) + int(product_code[2]))
    remainder = summa % 7
    if remainder == int(product_code[3]):
        return True
    else:
        return False
    
def main():
    print(f('1082'))
    print(f('2035'))
    print(f('1114'))
    print(f('7071'))
    print(f('704'))
    print(f('704451'))

if __name__ == '__main__':
    main()