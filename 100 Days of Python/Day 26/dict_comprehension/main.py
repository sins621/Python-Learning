from random import randint

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

student_scores = {student: randint(1, 100) for student in names}

print(student_scores)

passed_students = {student: score for (student, score) in student_scores.items() if score >= 80}

print(passed_students)