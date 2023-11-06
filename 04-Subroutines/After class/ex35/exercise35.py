import myfunction

number1 = int(input('Enter first number: '))
number2 = int(input('Enter second number: '))
operator = str(input('Enter operator: '))
result = myfunction.f(number1, number2, operator)

print(f'f({number1},{number2}, "{operator}") returns {result}')