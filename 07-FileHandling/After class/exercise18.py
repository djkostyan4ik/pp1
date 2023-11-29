fname = input('File name: ')
fhand = open(fname)
fhand2 = open('copy.txt','w')

fhand2.write(fhand.read())

fhand.close()
fhand2.close()