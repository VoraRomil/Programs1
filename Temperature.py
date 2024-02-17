#!/usr/bin/env python3

if __name__ == '__main__':
    def cel_to_fah(celsius):
        fahrenheit = celsius * 9/5 + 32
        return fahrenheit

# Yorkshire temperature in Celsius
celsius = 38.4

# Convert to Fahrenheit
fahrenheit = cel_to_fah(celsius)

# Display both temperatures
print(f"{celsius}°C is equivalent to {fahrenheit}°F")