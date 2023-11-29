import json
# json_file = open('movie_1.txt', 'r', encoding = 'utf-8')
# movie = json.load(json_file)
# json_file.close()


value = '''{
'title': 'Tron: Legacy',
'composer': 'Daft Punk',
'release_year': 2010,
'budget': 170000000,
'actors': null,
'won_oscar': false 
}'''

tron = json.loads(value)
print(tron)