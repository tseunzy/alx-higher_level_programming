# if/else statments

age = 18
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")


#to lookout for even and odd numbers
n = 11
if n % 2 == 0:
    print('Number is divisible by 2')
elif n % 3 == 0:
    print('Number is divisible by 3')
else:
    print('Number is neither divisible by 2 nor 3')
print('Done!')


#Grading of students scores using the if, elif 
score = int(input("Enter your score: "))
if score >= 70:
    print("Excellent! Grade A")
elif score >= 60:
    print("Very Good! Grade B")
elif score >= 50:
    print("Good! Grade C")
elif score >= 40:
    print("Pass! Grade D")
else:
    print("Fail! Grade F")
