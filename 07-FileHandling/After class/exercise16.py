fname = input('File name: ')
fhand = open(fname)
count = 0
for line in fhand:
    count += 1
print('Number of lines:',count)