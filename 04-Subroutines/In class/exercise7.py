weight = float(input('Enter your weight: '))
height = float(input('Enter your height: '))

lambda x: x == weight / (height/100)**2
bmi = lambda x: x == weight / height**2
bmi(81,182)











# lambda x: 3*x + 1
# g = lambda x: 3*x + 1
# g(2)

# full_name = lambda fn, ln: fn.strip().title() + ' ' + ln.strip().title()
# full_name('Kostya', 'Malinouski')