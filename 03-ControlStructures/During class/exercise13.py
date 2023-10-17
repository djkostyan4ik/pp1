number1 = int(input('Enter number 1: '))
number2 = int(input('Enter number 2: ')) 

if number1 > 0 and number2 > 0:
    print(f'Both of entered numbers are positive')

elif number1 < 0 and number2 < 0:
    print('Both of entered numbers are negative')

else:
    print(f'At least one of entered numbers {number1} and {number2} is not a negative')