file_name = input('Enter a file name: ')
fhand = open(file_name, 'r')
count = 0
for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    print(words[1])
    count += 1
print(f'There were {count} lines in the file with From as the first word')
