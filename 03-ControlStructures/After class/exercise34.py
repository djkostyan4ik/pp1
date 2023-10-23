whole_amount = int(input('Enter the amount in PLN: '))

fife_zlotych = int(whole_amount / 5)
remainder_from_fife = whole_amount % 5
two_zlotych = int(remainder_from_fife / 2)
remainder_from_two = remainder_from_fife % 2
one_zloty = int(remainder_from_two / 1)

print(f'The amount of PLN {whole_amount} in coins:\n5 zł - {fife_zlotych}\n2 zł - {two_zlotych}\n1 zł - {one_zloty}')