'''
(p1.py) The vending machine accepts
1, 2 and 5 PLN coins. Define the function
f(amount_to_pay) that returns the minimum number
of coins that can be used to pay
for the purchased product.
'''
def f(n):
    # coins = 0
    # coins += n//5
    # n = n % 5
    # coins += n//2
    # n = n % 2
    # coins += n

    fife_zlotych = int(n / 5)
    remainder_fife = n % 5
    two_zlotych = int(remainder_fife / 2)
    remainder_two = remainder_fife % 2
    one_zloty = int(remainder_two / 1)
    number_of_coins = fife_zlotych +  two_zlotych + one_zloty


    return number_of_coins

if __name__ == '__main__':
    #check your program in this place
    print(f(9))
    print(f(10))
    print(f(16))
