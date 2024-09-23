def fahrenheit_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius.
    Formula: (Fahrenheit - 32) * 5/9
    """
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

def main():
    try:
        fahrenheit_temp = float(input("Enter the temperature in Fahrenheit: "))
        celsius_temp = fahrenheit_to_celsius(fahrenheit_temp)
        print(f"{fahrenheit_temp:.2f}°F is approximately {celsius_temp:.2f}°C.")
    except ValueError:
        print("Oops! That doesn't look like a valid temperature. Please enter a numeric value.")
    else:
        print("Converted successfully! Stay cozy in those Celsius degrees!")

if __name__ == "__main__":
    main()
