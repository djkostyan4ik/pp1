fhand = open('MeatAndFish.txt')
fhand2 = open('GrainsAndBread.txt')
fhand3 = open('allproducts.txt','w')

fhand3.write(fhand.read())
fhand3.write('\n\n')
fhand3.write(fhand2.read())
# fhand3.write(fhand2.read())


fhand3.close()