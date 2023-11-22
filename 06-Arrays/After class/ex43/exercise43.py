import MyText
my_text = "An apple a day keeps the doctor away"
print('Text:',my_text)
print("Number of words:",MyText.text(my_text))
print("Words from the longest:",','.join(map(str,MyText.ordered(my_text))))
print("Words ordered alphabetically:",','.join(map(str,MyText.alphabeticall(my_text))))