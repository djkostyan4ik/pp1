
def  numbers(n):
    lista = ''
    for i in range (1, n+1):
        lista += str(i) + ' '
    return (f'Numbers <1, {n}>: {lista}')

my_number = int(input('Enter the range: '))
print(numbers(my_number))