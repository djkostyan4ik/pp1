def f(card_number):
    masked_part = '*' * 10
    result = card_number[0:2] + masked_part + card_number[-4:]

    return result

if __name__ == '__main__':
    print(f('5290312400019022'))