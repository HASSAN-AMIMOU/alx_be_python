# robust_division_calculator.py

def safe_divide(numerator, denominator):
    # Check if both numerator and denominator are numeric
    if not numerator.replace('.', '', 1).isdigit() or not denominator.replace('.', '', 1).isdigit():
        return "Error: Please enter numeric values only."
    
    # Convert inputs to float
    numerator = float(numerator)
    denominator = float(denominator)

    # Check for division by zero
    if denominator == 0:
        return "Error: Cannot divide by zero."
    
    # Perform division
    result = numerator / denominator
    return f"The result of the division is {result}"
