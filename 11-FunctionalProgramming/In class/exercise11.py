distance = int(input('Enter distance in km: '))
hours = int(input('Enter number of travel hours: '))
minutes = int(input('Enter number of travel minutes: '))

avg_speed = lambda distance,hours,minutes: f'Average speed: {round(distance/(hours + (minutes/60)),1)} km/h'

print(avg_speed(distance,hours,minutes))