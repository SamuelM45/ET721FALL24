"""
Samuel Martinez
Lab 3, Python Review
"""

print("------- Example 1: control flow -------")

labs = int(input("Enter labs grade: "))
exams = int(input("Enter exams' grade: ")) 
gpa = ''
finalgrade = 0

if 0 <= labs <= 100 and 0 <= exams <= 100:
    
    finalgrade = (labs + exams) / 2
    
    if 90 <= finalgrade <= 100:
        gpa = 'A'
    elif 80 <= finalgrade < 90:
        gpa = 'B'
    elif 70 <= finalgrade < 80:
        gpa = 'C'
    elif 60 <= finalgrade < 70:
        gpa = 'D'
    else:  
        gpa = 'F'
else:
    if not (0 <= labs <= 100) and not (0 <= exams <= 100):
        print(f"Grades for labs = {labs} and exams = {exams} are invalid")
    elif not (0 <= labs <= 100):
        print(f"Grade for labs {labs} is invalid")
    elif not (0 <= exams <= 100):
        print(f"Grade for exams {exams} is invalid")
    gpa = 'UNDEFINED'


print(f"Your final grade for the class is: {finalgrade} = {gpa}")

