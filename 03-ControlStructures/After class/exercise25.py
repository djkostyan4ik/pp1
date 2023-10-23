purchased_number = int(input('Number of products purchased: '))
product_price = float(input('Product price: '))
if purchased_number > 2:
    whole_amount = float((2 * product_price) + (purchased_number - 2) * (product_price * 0.75))
    print(f'Amount to pay: {whole_amount}')

elif 0 < purchased_number <= 2:
    print(f'Amount to pay: {purchased_number * product_price}')
else:
    print('Wrong number')