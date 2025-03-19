
def check_temperature(kelvin):
    """
    Raises a ValueError if an invalid temperature in Kelvin is given.

    :param kelvin:
    """

    if kelvin < 0.0:
        # Invalid temperature, below absolute zero
        raise ValueError("Invalid temperature")

def convert_fahrenheit(fahrenheit):
    """
    Convert given temperature in Fahrenheit to Celsius and Kelvin.

    Arguments:
    :param fahrenheit: temperature in Fahrenheit.

    Output
    :return: celsius: temperature in Celsius.
    :return: kevlin: temperature in Kelvin.
    """

    # Convert Fahrenheit to Celsius
    celsius = (fahrenheit - 32) * (5 / 9)

    # Convert Celsius to Kelvin
    kelvin = celsius + 273.15

    # Check if the temperature is valid.
    check_temperature(kelvin)

    return celsius, kelvin


def convert_celsius(celsius: float) -> float:
    """
    Convert given temperature in Celsius to Fahrenheit and Kelvin.

    Arguments
        :param celsius: temperature in Celsius.

    Returns:
        :return: fahrenheit: temperature in Fahrenheit.
        :return: kelvin: temperature in Kelvin.
    """

    # Convert Celsius to Fahrenheit.
    fahrenheit = (celsius * (9 / 5)) + 32

    # Convert Celsius to Kelvin
    kelvin = celsius + 273.15

    # Check if the temperature is valid.
    check_temperature(kelvin)

    return fahrenheit, kelvin


def convert_kelvin(kelvin):
    """
    Convert given temperature in Kelvin to Fahrenheit and Celsius.

    Arguments:
    :param kelvin: temperature in Kelvin.

    Output
    :return: fahrenheit: temperature in Fahrenheit.
    :return: celsius: temperature in Celsius.
    """

    # Convert Kelvin to Celsius
    celsius = kelvin - 273.15

    # Convert Celsius to Fahrenheit.
    fahrenheit = (celsius * (9 / 5)) + 32

    # Check if the temperature is valid.
    check_temperature(kelvin)

    return fahrenheit, celsius




# def convert_temperature(temperature, unit):
#     if unit == "F":
#         # Convert Fahrenheit to Celsius
#         celsius = (temperature - 32) * (5 / 9)
#         if celsius < -273.15:
#             # Invalid temperature, below absolute zero
#             return "Invalid temperature"
#         else:
#             # Convert Celsius to Kelvin
#             kelvin = celsius + 273.15
#             if kelvin < 0:
#                 # Invalid temperature, below absolute zero
#                 return "Invalid temperature"
#             else:
#                 fahrenheit = (celsius * (9 / 5)) + 32
#                 if fahrenheit < -459.67:
#                     # Invalid temperature, below absolute zero
#                     return "Invalid temperature"
#                 else:
#                     return celsius, kelvin
#     elif unit == "C":
#         # Convert Celsius to Fahrenheit
#         fahrenheit = (temperature * (9 / 5)) + 32
#         if fahrenheit < -459.67:
#             # Invalid temperature, below absolute zero
#             return "Invalid temperature"
#         else:
#             # Convert Celsius to Kelvin
#             kelvin = temperature + 273.15
#             if kelvin < 0:
#                 # Invalid temperature, below absolute zero
#                 return "Invalid temperature"
#             else:
#                 return fahrenheit, kelvin
#     elif unit == "K":
#         # Convert Kelvin to Celsius
#         celsius = temperature - 273.15
#         if celsius < -273.15:
#             # Invalid temperature, below absolute zero
#             return "Invalid temperature"
#         else:
#             # Convert Celsius to Fahrenheit
#             fahrenheit = (celsius * (9 / 5)) + 32
#             if fahrenheit < -459.67:
#                 # Invalid temperature, below absolute zero
#                 return "Invalid temperature"
#             else:
#                 return celsius, fahrenheit
#     else:
#         return "Invalid unit"

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(convert_celsius(15))

