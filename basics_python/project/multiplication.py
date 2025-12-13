
# a multiplication table 

number = int(input('Enter a number: '))

for i in range(1, 13):
    print(f'{number:2} x {i:2} = {number * i:3}') #i had to format the :4width for better alignment


