time = 0
time1 = 0
time2 = 0
washing_product = input('Enter a washing product: \n\n1.jacket\n2.underwear\n3.shoes\n\n')
rinse = int(input('Do you want an additional rinse?\n\n1 for Yes\n2 for No\n\n'))
spin = int(input('Do you want an additional spin?\n\n1 for Yes\n2 for No\n\n'))

if washing_product == 'jacket':
    time += 40
elif washing_product == 'underwear':
    time += 70
elif washing_product == 'shoes':
    time += 20
else:
    print('Choose the right product')


print(f'washing_product = "{washing_product}"')

if rinse == 1:
    time1 += 15
    print('rinse =',True)
else:
    time1 += 0
    print('rinse =',False)




if spin == 1:
    time2 += 9
    print('spin =',True)
else:
    time2 += 0
    print('spin =',False)


total_time = time + time1 + time2

print(f'Total washing time: {total_time}')