import range

x = int(input('Enter the begining number of the range: '))
y = int(input('Enter the end number of the range: '))
number = int(input('A number: '))

checking = range.range(x, y, number)

print(f'Number {number} in the range <{x},{y}>: {checking}')