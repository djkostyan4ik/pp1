import random

die = random.randint(1,6)

user_number = int(input('Try to guess and enter your number: '))

if user_number == die:
    print ('True')
else:
    print ('False')
print(f'Die number: {die}')
