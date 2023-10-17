try:
    hour = float(input('Enter Hours: '))
    rate = int(input('Enter Rate: '))
    if hour <= 40:
        pay = hour * rate
    else:
        pay = (hour - 40) * (1.5 * rate) + (40 * rate)
    print(f'Pay: {pay}')
except:
    print('Error, please enter a numeric input')