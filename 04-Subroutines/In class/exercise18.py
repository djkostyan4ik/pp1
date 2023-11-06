def numbers (n):
    list = ''
    for i in range(1, n + 1):
        list += ' ' + str(i)
    return(f'Numbers <1, {n}>: {list}')

n = int(input('Enter a range: '))
print(numbers(n))