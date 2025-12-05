
#add function 
def add(x, y):
    return x + y
#substraction function
def sub(a, b):
    return a - b

#to return multiple opereation, with to parameter
def add_sub_mul(a, b):
    return a+b, a-b, a*b

#to square a number 
def squar(a):
    return a**2

#even function
def is_even(a):
    return a % 2 == 0

#to chech if a character is a vowel 
def is_vowel(char):
    return char.lower() in {'a', 'e', 'i', 'o', 'u'}


def greet(name, greeting='Hello'):
    print(f'{greeting}, {name}!')

greet('felix')
print(is_vowel('i'))
print(is_even(8))

#simple use of function 
x = 20
y = 30
sum = add_sub_mul(x, y)
sum1 = list(sum)
sum1.append(96)
print(sum1)

numbers = (2, 4, 5, 9, 1, 3, 4, 6)
result = list(filter(is_even, numbers)) #using the filter function and my own function is_even

print(result)