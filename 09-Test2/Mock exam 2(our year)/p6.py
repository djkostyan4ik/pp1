import json

def f(years, course):
   with open("data.json", "r", encoding="UTF-8") as file:
      data = json.load(file)
      count = 0
      for student in data:
         if student["age"] == years:
               for stud_course in student["studies"]["courses"]:
                  if stud_course["name"] == course:
                     grade_average = sum(stud_course["grades"])/len(stud_course["grades"])
                     if grade_average >= 4:
                        count +=1
      return count
      
print(f(19,'programming'))
