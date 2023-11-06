def read_number():
    number1 = int(input('Enter a number: '))
    if number1 > 10:
        print('You need to enter only one-digit numbers!!!')
        exit(number1)
    return number1
    