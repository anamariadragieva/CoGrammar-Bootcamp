"""
This program calculates a user's total holiday cost, including plane, hotel and car rental cost.
"""

def plane_cost(city_flight):
    """
    Calculate the cost of the flight based on the chosen city.

    Args:
        city_flight (str): The city the user will be flying to.

    Returns:
        integer: Cost of the flight.
    """
    # Using a dictionary for better readability that if/else statements 
    city_prices = {
        "New York": 350,
        "Paris": 569,
        "London": 487,
        "Tokyo": 895
    }
    return city_prices.get(city_flight, 0)


def hotel_cost(num_nights):
    """
    Calculate the total cost for the hotel stay.

    Args:
        num_nights (int): Number of nights the user will stay at the hotel.

    Returns:
        float: Total cost of the hotel stay.
    """
    price_per_night = 129
    return num_nights * price_per_night


def car_rental(rental_days):
    """
    Calculate the total cost of the car rental.

    Args:
        rental_days (int): Number of days the user will be hiring a car.

    Returns:
        float: Total cost of the car rental.
    """
    daily_rental_cost = 65
    return rental_days * daily_rental_cost


def holiday_cost(city_flight, num_nights, rental_days):
    """
    Calculate the total cost of the holiday.

    Args:
        city_flight (str): The city the user will be flying to.
        num_nights (int): Number of nights the user will stay at the hotel.
        rental_days (int): Number of days the user will be hiring a car.

    Returns:
        float: Total cost of the holiday.
    """
    total_plane_cost = plane_cost(city_flight)
    total_hotel_cost = hotel_cost(num_nights)
    total_car_rental_cost = car_rental(rental_days)
    return total_hotel_cost + total_plane_cost + total_car_rental_cost


# User inputs
city_flight = input("Select the city you want to fly to:\n- New York\n- Paris\n- London\n- Tokyo\n")
num_nights = int(input("\nHow many nights will you be staying at a hotel? "))
rental_days = int(input("\nHow many days do you want to rent a car for? "))

# Calculate total holiday cost
total_cost = holiday_cost(city_flight, num_nights, rental_days)

# Print holiday details
print(f"""\n\nYour upcoming holiday details:
    \n\nDestination: {city_flight}
    \nNumber of nights: {num_nights}
    \nNumber of days for car rental: {rental_days}
    \n\nTotal holiday cost: £{total_cost}""")

