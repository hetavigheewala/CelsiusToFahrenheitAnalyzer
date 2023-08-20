
# Date - 7/25/2023


def get_num_readings():
    # Function to ask the user for the number of temperature readings
    while True:
        try:
            num_readings = int(input("Enter the number of temperature readings (between 1 and 50): "))
            if 1 <= num_readings <= 50:
                return num_readings
            else:
                print("Invalid input.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def celsius_to_fahrenheit(celsius):
    # Function to convert temperature from Celsius to Fahrenheit
    # Using the formula Fahrenheit = 9 / 5 * Celsius + 32
    # Rounding the result to 2 decimal places using round() function
    return round(9 / 5 * celsius + 32, 2)

def display_message(fahrenheit):
    # Function to display a message based on the Fahrenheit temperature
    # The function returns a message string based on the given criteria
    if fahrenheit < 40:
        return "Cold"
    elif 40 <= fahrenheit <= 80:
        return "Okay"
    else:
        return "Hot"

def main():
    # Main function to drive the program's execution

    num_readings = get_num_readings()  # Call get_num_readings() to get the number of temperature readings

    sum_fahrenheit = 0
    sum_celsius = 0

    # Loop to process each temperature reading
    for i in range(num_readings):
        while True:
            try:
                celsius = float(input("Enter temperature in degrees Celsius: "))  # Prompt for temperature in Celsius
                if -100 <= celsius <= 100:
                    break
                else:
                    print("Invalid input. Please enter a temperature between -100 and 100 degrees Celsius.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        fahrenheit = celsius_to_fahrenheit(celsius)  # Convert Celsius to Fahrenheit using celsius_to_fahrenheit()
        print(f"Degrees in Fahrenheit = {fahrenheit:.2f}\n")  # Display the Fahrenheit temperature
        print(display_message(fahrenheit))  # Display the corresponding message using display_message()
        print()

        sum_fahrenheit += fahrenheit  # Accumulate the Fahrenheit temperature for calculating average later
        sum_celsius += celsius  # Accumulate the Celsius temperature for calculating average later

    average_fahrenheit = sum_fahrenheit / num_readings  # Calculate the average Fahrenheit temperature
    average_celsius = sum_celsius / num_readings  # Calculate the average Celsius temperature

    print(f"Average of temperature in Fahrenheit is {average_fahrenheit:.2f}")  # Display the average Fahrenheit temperature
    print(f"Average of temperature in Celsius is {average_celsius:.2f}")  # Display the average Celsius temperature

if __name__ == "__main__":
    main()  # Call the main() function to start the program execution
