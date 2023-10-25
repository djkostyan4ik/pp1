dec = int(input('Enter decimal number: '))
pre_bin = str()
div = dec
while dec:
    if dec % 2 != 0:
        pre_bin += '1'
    else:
        pre_bin += '0'
    dec = dec // 2

bin = ''
for i in pre_bin:
    bin += pre_bin[-1]
    pre_bin = pre_bin[:-1]

print(f'{div}(10) = {bin}(2)')