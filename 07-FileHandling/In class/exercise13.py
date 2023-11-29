movies_titles = ['Spider-Man', 'Batman', 'Deadpool','Avengers', 'Iron-Man']
result = ''
for element in movies_titles:
    result += str(element) + '\n'
file = open('movies.txt','w')
file.write(result)
file = open('movies.txt','r')
file_content = file.read()
print(file_content)
file.close()