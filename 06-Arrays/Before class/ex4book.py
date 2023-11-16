user_data = input('Which files? ')
fhand = open(user_data, 'r')
word_list = []
for line in fhand:
    words = line.split()
    for each_word in words:
        # each_word = each_word.lower()
        if each_word in word_list:
            pass
        else:
            word_list.append(each_word)

print(sorted(word_list))