

'''Convert temperature between:
Celsius ↔ Fahrenheit
°F = (°C × 9/5) + 32
°C = (°F − 32) × 5/9'''

print('Temperature converter')
print('1. Celsius to Fahrenheit')
print('2. Fahrenheit to Celsius')

choice = input('Choose option (1 or 2): ')

temp = float(input("Enter temperature: "))

if choice == '1':
    result = (temp * 9/5) + 32
    print('Temperature in Fahrenheit:', result)
elif choice == '2':
    result = (temp - 32) * 5/9
    print('Temperature in Celsius:', result)
else:
    print('Invalid choice')
