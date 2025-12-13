
# S.S.S 3 Student grading decision making
score = int(input('Enter student score: '))

if score < 0 or score > 100:
    grade = 'Invalid score'
elif score >= 70:
    grade = 'A'
elif score >= 60:
    grade = 'B'
elif score >= 50:
    grade = 'C'
elif score >= 45:
    grade = 'D'
else:
    grade = 'F'

print('Grade:', grade)
