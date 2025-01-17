
def safe_divide(numerator, denominator):
    try:
        # Attempt to convert inputs to floats
        numerator = float(numerator)
        denominator = float(denominator)

        # Check for division by zero
        if denominator == 0:
            return "Error: Cannot divide by zero."
        
        # Perform the division and return the result
        result = numerator / denominator
        return f"The result of the division is {result}"

    except ValueError:
        return "Error: Please enter numeric values only."
