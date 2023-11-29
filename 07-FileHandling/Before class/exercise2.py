# fhand = open('mbox.txt')
# print(fhand)

# fhand = open('mbox-short.txt')
# count = 0
# for line in fhand:
#     count = count + 1
# print('Line Count:', count)


# fhand = open('mbox-short.txt')
# inp = fhand.read()
# print(len(inp))
# print(inp[:20])

# fhand = open('mbox-short.txt')
# for line in fhand:
#     if line.startswith('From:'):
#         print(line)

# fhand = open('mbox-short.txt')
# for line in fhand:
#     line = line.rstrip()
#     if line.startswith('From:'):
#         print(line)

# fhand = open('mbox-short.txt')
# for line in fhand:
#     line = line.rstrip()
#     # Skip 'uninteresting lines'
#     if not line.startswith('From:'):
#         continue
#     # Process our 'interesting' line
#     print(line)


# fhand = open('mbox-short.txt')
# for line in fhand:
#     line = line.rstrip()
#     if line.find('@uct.ac.za') == -1: continue
#     print(line)


# fname = input('Enter the file name: ')
# fhand = open(fname)
# count = 0
# for line in fhand:
#     if line.startswith('Subject:'):
#         count = count + 1
# print('There were', count, 'subject lines in', fname)




# fname = input('Enter the file name: ')
# try:
#     fhand = open(fname)
# except:
#     print('File cannot be opened:', fname)
#     exit()
# count = 0
# for line in fhand:
#     if line.startswith('Subject:'):
#         count = count + 1
# print('There were', count, 'subject lines in', fname)


fout = open('output.txt','w')
line1 = "This here's the wattle,\n"
fout.write(line1)
line2 = 'the eblem of our land.\n'
fout.write(line2)
print(fout)
fout.close()