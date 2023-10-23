bank_buys = float((input('Bank buys EUR: ')))

bank_sells = float(input('Bank sells EUR: '))

spread = float((bank_sells - bank_buys))

print(f'Spread: {round(spread, 5)}0')