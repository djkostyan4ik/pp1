file = open ('numbers.txt','r')
sum = 0
for line in file:
    sum += int(line)
    print(line, end = '')
print()
print("Sum:",sum)
file.close()