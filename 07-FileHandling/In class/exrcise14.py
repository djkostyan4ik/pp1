file = open("shopping.txt",'w')
read_product = True
counter = 0
while read_product:
    product = input("Enter product name: ")
    if product != "":
        counter += 1
        file.write(f'{counter}.{product}' + '\n')
    else:
        read_product = False

file = open('shopping.txt','r')
file_content = file.read()
print(file_content)
file.close()
