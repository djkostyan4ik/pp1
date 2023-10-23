a = int(input('Enter the width (a): '))
b = int(input('Enter the height (b): '))
for i in range(a):
    if i == 0 or i == a - 1:
        print('*' * b)
    else:
        print('*' + ' ' * (b - 2) + '*')