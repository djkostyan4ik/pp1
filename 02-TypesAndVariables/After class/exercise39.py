price = round(float(input('Enter price: ')),3)
discount = int(input('Enter discount %: '))
after_disc = round(price - (price * discount / 100),2)
print (f'Price with discount: {after_disc}')
reduction = round(price - after_disc, 2)
print(f'Reduction: {reduction}')