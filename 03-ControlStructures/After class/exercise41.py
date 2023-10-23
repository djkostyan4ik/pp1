pin_code = '0805'

attempts = 0
while attempts < 3:
    entered_pin = str(input('Enter the PIN code: '))


    if entered_pin == pin_code:
        print('PIN code is correct. Access allowed.')
        break
    else:
        print('Incorrect...')
        attempts += 1
        
        
if attempts == 3:
    print('Incorrect...')
    print('Sorry, your payment card has been blocked.')