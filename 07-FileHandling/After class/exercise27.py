import re
text = 'To be, or not to be, that is the question'
words = re.findall('[a-zA-z]+', text)
print(len(words))