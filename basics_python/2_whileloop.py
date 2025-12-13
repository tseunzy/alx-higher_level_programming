
#while loop using the continue function to skip a number
i = 0
while i < 10:
    if i == 3 or i == 5:
        i += 1
        continue
    print(i, end=' ')
    i += 1

print('\n===============')

#using the break function to terminate the loop if found
languages = ['c##', 'python', 'c#', 'java']
i = 0
while i < len(languages):
    if languages[i] == 'c##':
        i += 1
        print('i like c##')
        break
else:
    print('coding is not my thing')

print('\n===============')
#from the FOR loop, the languages is already in str so it will print the str in the list
languages = ['c', 'python', 'c##', 'java']
for i in languages:
    print(i)

print('\n===============')
#using the split function to calculate the number of words
sentence = "i alooking for the breath, where is it"
sum = 0
for i in sentence.split():
    sum += 1

print(sum)  