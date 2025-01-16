student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

# - Scores 91 - 100: Grade = "Outstanding" 

# - Scores 81 - 90: Grade = "Exceeds Expectations" 

# - Scores 71 - 80: Grade = "Acceptable" 

# - Scores 70 or lower: Grade = "Fail" 

def score_to_grade(student_scores, student):
    score = student_scores[student]
    if score <= 70:
        return "Fail"
    elif score <= 80:
        return "Acceptable"
    elif score <= 90:
        return "Exceeds Expectations"
    else:
        return "Outstanding"

student_grades = {}

for student in student_scores:
    student_grades[student] = score_to_grade(student_scores, student)

print(student_grades)
