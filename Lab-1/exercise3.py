# Problem 3. Input a temperature in Celsius and convert it to Fahrenheit and Kelvin using the formulas:
# F = (C ×9/5) + 32, K= C + 273.15


celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

kelvin = celsius + 273.15

print("Temperature in Celsius:", celsius)
print("Temperature in Fahrenheit:", fahrenheit)
print("Temperature in Kelvin:", kelvin)
