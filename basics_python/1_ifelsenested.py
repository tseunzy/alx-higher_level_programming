
# this if a nested if statement
age = 20
nationality = 'Nigerian'
if age > 18:
    if age < 30:
        if nationality == 'Nigerian':
            print('You are qualify for this Exam')

print('===============')


#using the AND with IF statement
age = 20
nationality = 'Nigerian'
if age > 18 and age < 30 and nationality == 'Nigerian':
    print('You are qualify for this Exam')

print('===============')


# LOGICAL AND WITH IF-ELSE STATEMENT
age = 41
nationality = 'Nigerian'
if age > 18 and age < 30 and nationality == 'Nigerian':
    print('You are qualify for this Exam')
else:
    print('You are not eligible for the exam')


print('===============')


# LOGICAL AND WITH IF-ELIF-ELSE STATEMENT
age = int(input('whats your age?'))
nationality = 'American'
if age > 18 and age < 30 and nationality == 'Nigerian':
    print('You are qualify for this Exam. Exam fee is 2000 naira')
elif age > 18 and age < 30 and nationality == 'American':
    print('You are not eligible for the exam. Exam fee is $50')
else:
    print('You are not eligible for the exam.')