
#List of days in the week
Day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
today = 'Monday'

if today == 'sunday' or today == 'saturday':
    print('its weekend!')
elif today in Day:  #I used the in function to check if today is in day
    print('its weekday!')
else:
    print('thets not among the days of the week')


print('=' * 20)

fruits = ['apple', 'banana', 'orange', 'peal' ]

for fruit in fruits:
    print(fruit, end=",")


print('\n==================')

items = ['rice', 'beans', 'yam', 'oil']
target = 'yam'

for item in items:
    if item == target:
        print('Found:', item)
        break

print('================')

names = ['John', 'Mary', 'James','Rebecca']

for i in range(len(names)): #using the range function 
    print(f'{i}. {names[i]}') # i used this instead of enumerator right


print('================')

#checking for student that pass and fail
scores = [45, 78, 90, 56]

for score in scores:
    if score >= 50:
        print(score, 'Pass')
    else:
        print(score, 'Fail')

print('================')


#total in a list, using the in function
prices = [250, 150, 300, 500]

total = 0
for amount in prices:
    total += amount

print('Total =', total)


print('================')

#SQUARE OF THE NUMBERS IN THE LIST IS APPEND TO AN NEW LIST
numbers = [1, 2, 3, 4]
squares = []

for n in numbers:
    squares.append(n * n)

print(squares)

print('================')

names = ['fred', 'matt', 'simon', 'elijah', 'francis', 'michael']
names.remove('michael')
retrn = names.pop() #the pop return the item return remove and return the last item as tuple
names.extend(['lanre', 'deola', 'remi']) #i use the extend func to add multiple list
names.append('manuel') #add an item to the last
names.insert(len(names)-1, 'matter' ) #inseat in that position
names[1] = 'jude' #replace
del names[1] #delete, while i use clear to delete all element 
print(names)
print(retrn)