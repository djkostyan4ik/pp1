decimal_number = int(input('Enter decimal number: '))
binary_number = ''
quotient = decimal_number
while quotient > 0:
    remainder = quotient % 2
    binary_number = str(remainder) + binary_number
    quotient = quotient // 2
print(f"{decimal_number}(10) = {binary_number}(2)")