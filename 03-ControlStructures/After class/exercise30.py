time_24format = input('Enter time (24-hour format): ')
hours, minutes = map(int, time_24format.split(':'))

if hours < 12:
    period = 'am'
else:
    period = 'pm'

if hours == 0:
    hours_12_format = 12
elif hours <= 12:
    hours_12_format = hours
else:
    hours_12_format = hours - 12


print(f'Time in 12-hour format: {hours_12_format}:{minutes}{period}')
