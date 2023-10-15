bank_buys = float(input(f'Bank buys EUR: ')) 

bank_sells = float(input('Bank sells EUR: '))

spread = round(bank_sells - bank_buys, 5)

print(f'Spread: {spread}')