current_price = float(input('Enter the current product price: '))
previous_price = float(input('Enter previous product price: '))

procent = 100 - ((current_price/previous_price) * 100)

if procent >= 10:
    procent = int(procent)
    print('Buy the product!!')
    print(f'Product price reduced by {procent}%')
else:
    print('Wait for bigger discount')