import re
with open('pan-tadeusz.txt', encoding = 'UTF-8') as file:
    text = file.read()
    words = re.findall('[a-zA-Z]{6,}',text)


for i in words:
    print(i)