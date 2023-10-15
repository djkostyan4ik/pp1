import random

rolls = random.randint(1, 6)
for i in range (0, rolls):
    die = random.randint(1, 6)

print(f'Dice rolled: {rolls}')
    
if die == 1:
    print('Special number: True')
elif die == 6:
    print('Special number: True')
else:
    print('Special number: False')
print(f'Number on the dice: {die}')
