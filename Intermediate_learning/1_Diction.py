
#to access the 
person = {'name': 'Alice', 'age': 25, 'city': 'Lagos'}

for key in person:
    print(key, end=',')

print('\n==================')

person = {'name': 'Alice', 'age': 25, 'city': 'Lagos'}

for key in person.values(): #this show the values in the dictionary
    print(key, end=',')

print('\n==================')

person = {'name': 'Alice', 'age': 25, 'city': 'Lagos'}

for key in person.items(): #this show all the items in the dictionary
    print(key, end=',')

print('\n==================')

#I USED THE ISINSTANCE FUNCTION TO PRINT JUST THE STRING ITEMS
for key, value in person.items():
    if isinstance(value, str): 
        print(key, value)

print('\n==================')

scores = {
    'Oluwaseun': [80, 90],
    'Tunde': [75]
}

scores['Oluwaseun'].append(95)
scores['Tunde'].append(88)


print('\n==================')

print(scores)

student = {"name": "Lola", "age": 21, "course": "Math"}

name, age, course = student.values()

print(name, age, course)


print('================')

#Appending the names of my teacher into the dictionary
people = {
    'students': [],
    'teachers': []
}

for name in ['Alex', 'Maria', 'Grace']:
    people['students'].append(name)
for name in ['Emeka', 'Martins']:
    people['teachers'].append(name)

print(people)


print('================')

student = {'name': 'John', 'age': 20}
student['grade'] = 'A' #add a key-value to the dict
print(student)

student.update({'school': 'LASUED', 'level': 300}) #add multiply pairs
student.pop('school') #delete school
student['age'] = 25  #replace the value of keyage by 25
print(student)
