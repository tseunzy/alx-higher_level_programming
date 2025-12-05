#SQUARE OF THE NUMBERS IN THE LIST IS APPEND TO AN NEW LIST using comprehension metthod
numbers = [1, 2, 3, 4]
squares = [n * n for n in numbers]

print(squares)


print('================')
#to print the largest number in the list
nums = [5, 9, 3, 8, 2]
largest = nums[0]
num = [n for n in nums if n > largest]

print(num)


print('================')
#using the zip function to combine two list together
names = {'id1': 'John', 'id2': 'Mary'}
ages  = {'id1': 20, 'id2': 22}

combined = {k: (names[k], ages[k]) for k in names}

print(combined)


print('================')
#Appending the names of my teacher into the dictionary

logs = {
    'Oluwaseun': [],
    'Aisha': []
}

logs['Oluwaseun'].append('2025-01-20 10:00AM')
logs['Oluwaseun'].append('2025-01-21 11:00AM')

logs['Aisha'].append('2025-01-21 09:00AM')

print(logs)

print('================')

students = {'Joy': 20, 'Mark': 22, 'Sade': 19}

filtered = {name: age for name, age in students.items() if age > 20}

print(filtered)

print('================')

#Replace all even and odd with 'even' and 'odd' respectively
list = [4, 16, 25, 81, 1, 9, 16, 36]
labels = ['even' if n % 2 == 0 else 'odd' for n in list ]
print(labels)

print('================')

#Keep only numbers that are divisible by both 2 and 3 using list comprehension
div_2__3 = [n for n in list if n % 2 == 0 and n % 3 == 0]
print(div_2__3)
