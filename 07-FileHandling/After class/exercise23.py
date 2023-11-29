fhand = open('mynumbers.txt','w')
for number in range(1,10):
    fhand.write(f"{number},{number**2},{number**3}\n")
fhand.close()
