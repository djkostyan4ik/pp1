import math

height_cm = input('Enter your height: ')
height_feet = math.floor(height_cm / 30.48)
height_cm2 = height_cm - round(height_feet * 30.48)
height_inches = round(height_cm2 / 2.54)
print(f'I am {height_cm} tall, i.e. {height_feet} feet and {height_inches} inches')



