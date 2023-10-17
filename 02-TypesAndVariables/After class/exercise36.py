bank_buys = float(input('Bank buys EUR: ')) 

bank_sells = float(input('Bank sells EUR: '))

spread = round(bank_sells - bank_buys, 4)

print(f'Spread: {spread}')