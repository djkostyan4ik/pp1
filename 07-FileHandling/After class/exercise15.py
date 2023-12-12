# file = open('filename.txt','w')
# file.write('Doc1.docx\nfjshdff.jpg')
# file.close()

# file = open("filename.txt")
# for line in file:
#      print(line, end="")
# file.close()


with open('filename.txt') as file:
    for line in file:
        print(line,end = '')
file.close()