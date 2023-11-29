fhand = open('mbox-short.txt')
for line in fhand:
    shout = line.strip().upper()
    print(shout)