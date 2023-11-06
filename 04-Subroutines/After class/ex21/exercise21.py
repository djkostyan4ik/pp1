import mymath
import mykeyboard

my_number = mykeyboard.read_number()
bot_number = mymath.generate_number()

print(f'Computer number: {bot_number}')

if my_number == bot_number:
    print('You won the game!!')
else:
    print('You lost the game.')