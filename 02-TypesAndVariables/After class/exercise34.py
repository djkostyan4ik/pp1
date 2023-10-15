speed = float(input('Enter vehicle speed in km/h: '))
if 40 <= speed <= 140:
    print('Speed is valid: True')
elif speed < 40:
    print ('Your speed is too low')
else:
    print('Speed is valid: False')