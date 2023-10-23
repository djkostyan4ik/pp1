car_speed = float(input('Enter car speed: '))
speed_limit_min = 40
speed_limit_max = 140
if speed_limit_min <= car_speed <= speed_limit_max:
    print('Keep the same speed')
elif car_speed > 140:
    print('Warning: your speed is too high!!')
else:
    print('Warning: invalid car speed!!')