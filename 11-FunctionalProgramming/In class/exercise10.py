distance = int(input('Enter distance in km: '))
hours = int(input('Enter number of travel hours: '))
minutes = int(input('Enter number of travel minutes: '))
def avg_speed(distance,hours,minutes):
    min_to_hours = minutes / 60
    average = distance / (hours + min_to_hours)
    return f'Average speed: {round(average,1)} km/h'


print(avg_speed(distance,hours,minutes))