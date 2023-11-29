fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened: ',fname)
    quit()
total = 0
count = 0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        count += 1
        colpos = line.find(':')
        number = line[colpos + 1:].strip()
        reszta = float(number)
        total += reszta
average = total / count

print('Average spam confidence: ',average)