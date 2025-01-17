# temp_conversion_tool.py

# Define Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Implement Conversion Functions
def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# User Interaction
def main():
    while True:
        try:
            # Prompt the user for temperature input
            temp = input("Enter the temperature to convert (or type 'exit' to quit): ").strip()
            if temp.lower() == 'exit':
                print("Exiting the program. Goodbye!")
                break

            if not temp.replace('.', '', 1).lstrip('-').isdigit():
                raise ValueError("Invalid temperature. Please enter a numeric value.")

            temp = float(temp)
            unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

            if unit == "F":
                converted_temp = convert_to_celsius(temp)
                print(f"{temp}°F is {converted_temp:.2f}°C")
            elif unit == "C":
                converted_temp = convert_to_fahrenheit(temp)
                print(f"{temp}°C is {converted_temp:.2f}°F")
            else:
                raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()