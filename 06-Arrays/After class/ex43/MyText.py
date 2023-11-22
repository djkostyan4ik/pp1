def text(my_text):
    words = len(my_text.split())
    return words

def ordered(my_text):
    words = my_text.split()
    return sorted(words, reverse=True, key = len)

def alphabeticall(my_text):
    words = my_text.split()
    return sorted(words, key = str.lower)