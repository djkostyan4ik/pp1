suma = 0
count = 0
for number in range(1, 10):
    if number % 2 == 0:
        suma += number
        print(number)
print(f'The sum is {suma}')