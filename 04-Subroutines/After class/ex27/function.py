
# def f(card_number, start_number = 2, end_number = 4, char = '*'):
#     card_number_length = len(card_number)
#     mask = card_number_length - start_number - end_number
#     return (card_number[:start_number] + (char * mask) + card_number[-end_number:])


def f(card_number):
    masked_part = ''
    for i in range(11):
        masked_part += '*'
    result = card_number[0:2]+ masked_part + card_number[-4:]
    return result