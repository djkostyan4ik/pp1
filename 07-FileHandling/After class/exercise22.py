import random
fhand = open('random_numbers.txt','w')

rand_num = []

for number in range(1,50):
    rand_num.append(str(random.randint(100,999)) + '\n')
rand_num.append(str(random.randint(100,999)) + '\n')

fhand.writelines(rand_num)
fhand.close()