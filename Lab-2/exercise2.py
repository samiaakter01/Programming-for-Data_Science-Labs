# Problem 2 – Weekend Temperatures
# Create a tuple containing six temperature readings: three for Saturday and three for Sunday. 
# Use a for loop to display each reading and calculate the highest and lowest temperatures.


temperatures = (28, 31, 33, 27, 30, 32)

maximum = temperatures[0]
minimum = temperatures[0]

print("Weekend temperatures:")

for temperature in temperatures:
    print(temperature)

    if temperature > maximum:
        maximum = temperature
    
    if temperature < minimum:
        minimum = temperature
    


print("Highest temperature:", maximum)
print("Lowest temperature:", minimum)
