# Prompt the user to enter the temperature in Fahrenheit
degrees_fahrenheit = float(input("Enter temperature in Fahrenheit: "))

# Convert the temperature to Celsius using the formula
degrees_celsius = (degrees_fahrenheit - 32) * 5.0 / 9.0

# Print the result with an appropriate message
print(f"Temperature: {degrees_fahrenheit}F = {degrees_celsius}C")
