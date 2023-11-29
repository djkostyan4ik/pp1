import re
text = 'To be, or not to be, that is the question'
vovels = re.findall('[aeiouyAEIOUY]',text)
print(len(vovels))