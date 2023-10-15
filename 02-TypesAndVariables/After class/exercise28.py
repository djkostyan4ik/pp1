height = float(input('Enter your height in cm: '))
weight = float(input('Enter your weight in kg: '))
bmi = weight / (height / 100) ** 2
print (f'Your bmi index: {bmi}')

if 18.5 <= bmi <= 24.9:
    print('Correct weight: True')
else:
    print('Correct weight: False')
    