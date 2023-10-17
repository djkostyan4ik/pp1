speed_limit = int(140)
car_speed = int(input('Enter car speed km/h: '))

if car_speed > speed_limit:
    print('Warning: speed limit exceeded!!')
elif 0 < car_speed <= speed_limit:
    print('Keep the same speed')
else:
    print('You need to enter the right speed')
