for number in range(1,31):
    if number % 3 == 0 and number % 5 == 0:
        number = 'BINGO'
    elif number % 3 == 0:
        number = 'TREE'
    elif number % 5 == 0:
        number = 'FIVE'
    print(number, end = ' ')