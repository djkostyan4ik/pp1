def f(first_letter,last_letter):
    count = 0
    for word in open('data.txt', encoding = 'UTF-8').read().split():
        if first_letter in word[0] and last_letter in word[-1]:
            count += 1

    return count

if __name__ == '__main__':
    print(f('w','d'))
