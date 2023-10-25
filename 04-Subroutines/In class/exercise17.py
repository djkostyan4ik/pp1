def numbers(n1, n2, n3):
    if n1 != n2 and n1 != n3  and n2 != n3:
        return True
    else:
        return False
    
first_number = int(input('Enter first number: '))
second_number= int(input('Enter the second number: '))
third_number = int(input('Enter the third number: '))


if numbers(first_number, second_number, third_number):
    print(f'Numbers {first_number}, {second_number}, and {third_number} are different.')
else:
    print('Theu are the same.')