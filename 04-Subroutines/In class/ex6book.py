

def computepay(hrs, rt):
    if hrs > 40:
        pay = (hrs - 40) * 1.5 * rt + (40 * rt)
    else:
        pay = hrs * rt
    return pay

hours = float(input('Enter hours: '))
rate = float(input('Enter rate: '))
pay = (computepay(hours, rate))
print(f'Pay: {pay}')