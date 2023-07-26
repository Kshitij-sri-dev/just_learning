unit = input('Is this temperature in Celsius or Fahrenheit:')
temp = float(input('Enter the temp: '))

if unit == 'C':
    temp = round((9*temp) / 5 + 32, 1)
    print(f'The temperature is {temp}F°')
elif unit == 'F':
    temp = round((temp-32) * 5 / 9, 1)
    print(f'The temperature is {temp}C°')
else:
    print(f'{unit} is an invalid unit of supported units of temp.')
