name = "Anna May"
university = "Krakow University of Economics"
field = "Applied Informatics"

file = open("student.txt",'w')
file.write(name+"\n")
file = open("student.txt",'r')
file_content = file.read()
print(file_content)
file.close()