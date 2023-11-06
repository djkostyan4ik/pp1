def calculations (my_text, my_letter):
    count = 0
    for i in my_text:
        if i == my_letter:
            count += 1
    return count
