import json

student = {
    'student': True,
    'kierunek': 'Informatyka Stosowana',
    'zadań': 'dużo',
    'age' : 17
}

out_file = open('student.json','w')

json.dump(student,out_file,indent = 4)

out_file.close()