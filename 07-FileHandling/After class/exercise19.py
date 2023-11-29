fname = input('File name: ')
fhand = open(fname)
fhand2 = open('copylines.txt','w')

for line in fhand:
    fhand2.write(line)

fhand.close()
fhand2.close()