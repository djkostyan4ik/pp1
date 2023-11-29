# import re
# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.strip()
#     if re.search('From:',line):
#         print(line)


# import re
# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.strip()
#     if re.search('^From:',line):
#         print(line)




# # Search for lines that start with 'From'
# import re
# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     if re.search('^F..m:', line):
#         print(line)



# # Search for lines that start with From and have an at sign
# import re
# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     if re.search('^From:.+@', line):
#         print(line)



# import re
# s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
# lst = re.findall('\S+@\S+', s)
# print(lst)



# # Search for lines that have an at sign between characters
# import re
# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     x = re.findall('\S+@\S+', line)
#     if len(x) > 0:
#         print(x)


# Search for lines that have an at sign between characters
# import re
# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     x = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', line)
#     if len(x) > 0:
#         print(x)



# # Search for lines that start with 'X' followed by any non
# # whitespace characters and ':'
# # followed by a space and any number.
# # The number can include a decimal.
# import re
# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     if re.search('^X\S*: [0-9.]+', line):
#         print(line)



# # Search for lines that start with 'X' followed by any
# # non whitespace characters and ':' followed by a space
# # and any number. The number can include a decimal.
# # Then print the number if it is greater than zero.
# import re
# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     x = re.findall('^X\S*: ([0-9.]+)', line)
#     if len(x) > 0:
#         print(x)









# # Search for lines that start with 'Details: rev='
# # followed by numbers
# # Then print the number if one is found
# import re
# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     x = re.findall('^Details:.*rev=([0-9]+)', line)
#     if len(x) > 0:
#         print(x)




# Search for lines that start with From and a character
# followed by a two digit number between 00 and 99 followed by ':'
# Then print the number if one is found
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^From .* ([0-9][0-9]):', line)
    if len(x) > 0: print(x)


