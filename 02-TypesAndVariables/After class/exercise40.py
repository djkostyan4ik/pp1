card_num = input('Enter credit card numer: ')
sep_num = card_num[0:4] + " " + card_num[4:8] + " " + card_num[8:12] + " " + card_num[12:16]
print(f'Card number: {sep_num}')