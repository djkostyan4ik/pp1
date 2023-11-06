import calculations

my_text = str(input('Enter your text to count the amount of one letter in this text: '))
my_letter = str(input('Enter your letter: '))
amount = calculations.calculations(my_text, my_letter)

print(f"The number of letter '{my_letter}': {amount}")