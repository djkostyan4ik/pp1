def f(amount_to_pay):
    fife_zlotych = int(amount_to_pay / 5)
    remainder_from_fife = amount_to_pay % 5
    two_zlotych = int(remainder_from_fife / 2)
    remainder_from_two = remainder_from_fife % 2
    one_zloty = int(remainder_from_two / 1)
    number_of_coins = fife_zlotych + two_zlotych + one_zloty
    return number_of_coins