arr = [12, 6, 4, 9, 10]
# for element in arr:
#     print(f'{element}: {element * '*'}')

def star(element):
    element = str(element)
    if len(element) == 2:
        return f'{element}: {int(element) * '*'}'
    elif len(element) == 1:
        return f'{" " + element}: {int(element) * '*'}'
    else:
        return f'{element}: {int(element) * '*'}'

for element in arr:
    print(star(element))


# for element in arr:
#     print(star(element))
