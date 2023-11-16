my_list = []
while (True):
    input_number = input('Enter  a number: ')
    if input_number == 'done':
        break
    else:
        number = float(input_number)
        my_list.append(number)
print(f'Maximum: {max(my_list)}')
print(f'Minimum: {min(my_list)}')