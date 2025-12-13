

row = int(input('Enter number of rows: '))

for i in range(1, row+1):
    for space in range(row-i):
        print(' ', end=" ")
    for star in range(2*i-1):
        print('*', end=' ')
    print( )
for i in range(row-1, 0, -1):
    for space in range(row -i):
        print(' ', end=' ')
    for star in range(2 * i - 1):
        print('*', end=" ")
    print()


print('\n===================')

