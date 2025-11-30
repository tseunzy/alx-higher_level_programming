# IF THE BOOLEAN VALUE IS TRUE, THEN THE NOT OPERATOR RETURNS FALSE
x = False
if not x:
    print('x is false')

print('===============')

#LOGICAL NOT WITH THE STRING
#IF THE STING IS EMPTY, THE THE NOT OPERATOR RETURNS TRUE
name = 'john'
if not name:
    print('no name')
else:
    print(f'your name is {name}.')

print('===============')
#LOGICAL NOT WITH A LIST, DICT OR TUPLE
# JUST LIKE STRING
names = ['john', 'sarah', 'matter']
if not names:
    print('no names.')
else:
    print(f'ther are a total of {len(names)} names.')


print('===============')

# OPR AND IF STATEMENT
today = 'Sunday'
if today == 'Sunday' or today == 'Saturday':
    print('Its a weekend')


print('===============')
# OR AND IF-ELSE STATEMENT 

today = 'Monday'
if today == 'Sunday' or today == 'Saturday':
    print('Its a weekend')
else:
    print('its a weekday!')