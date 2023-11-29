fhand = open('numbers.txt','w')
numbers = []
for number in range(1,50):
    numbers.append(str(number) + '\n')

fhand.writelines(numbers)
fhand.close()