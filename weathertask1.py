def get_temperature():
    try:
        fahrenheit = float(input("Please enter the temperature in Fahrenheit: "))
        return fahrenheit
    except ValueError:
        print("Oops! That doesn't look like a valid temperature. Please enter a numeric value.")

def main():
    temperature_fahrenheit = get_temperature()
    print(f"You entered {temperature_fahrenheit:.2f}°F. Nice choice!")

if __name__ == "__main__":
    main()
