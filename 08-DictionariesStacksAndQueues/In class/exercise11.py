import json

movie = {
    'title': 'Spider-Man No Way Home',
    'year': '2021',
    'actor': {'leading': 'Tom Holland','supporting': 'Tobey Maguire'},
    'oscar': False,
    'genre': 'science-fiction'
}

out_file = open('favourited.json','w')

json.dump(movie,out_file, indent = 4)

out_file.close()