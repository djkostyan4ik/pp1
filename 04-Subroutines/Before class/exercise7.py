weight = float(input('Enter your weight: '))
height = float(input('Enter your height: '))

bmi = lambda weight, height: height / (weight / 100) ** 2
print(bmi(weight, height))



# lambda x: 3*x + 1
# g = lambda x: 3*x + 1
# g(2)

# full_name = lambda fn, ln: fn.strip().title() + ' ' + ln.strip().title()
# full_name('Kostya', 'Malinouski')