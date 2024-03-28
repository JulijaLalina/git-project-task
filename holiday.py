# Library with the flight info.

flight_price = {"london": 100,
           "dublin": 90,
           "paris": 80,
           "berlin": 110,
           "antwerp": 70,
           "budapest": 80,
           "madrid": 120,
           "rome": 90,
           "barcelona": 150,
           "geneva": 300}

# List of the cities in the lilbrary printed.

cities = list(flight_price.keys())

print(f"We have information for the following cities: {cities}")
print()

# Defining all functions outside of the loop to avoid defining them in each iteration.

def plane_cost(city_flight):
    ticket_price = flight_price[city_flight] # Ticket price is calculated by calling key;value pair from the dictionary.
    return ticket_price

def hotel_cost(num_nights):
    hotel_rate = 100 # Constant for hotel rate.
    hotel_price = hotel_rate * num_nights
    return hotel_price

def car_rental(rental_days):
    rate = 50 # Constant for the car rental rate.
    rental_cost = rental_days * rate
    return rental_cost

def holiday_cost(plane, hotel, car):
    total_holiday_cost = plane + hotel + car # Calculating the total as a sum of all costs. 
    return total_holiday_cost

# Function to check for valid integer inputs for the number of nights and day of car rental.

def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid integer.")

# Infinite loop that will allows for continuation check.

while True: 

    city_flight = input(f"Which city are you going to? Please choose from the list \n {cities}: ").lower().strip()
    print()

    while city_flight not in flight_price: # While loop to check if the input city is on the list and calculations can be made.
        
        print("Sorry we do not have flight price information for this destination.")
        city_flight = input("Choose another? : ").lower().strip()
        print()

    # Applying function to the inputs to check if they are a valid integer.
        
    num_nights = get_integer_input("How many nights are you staying? Please enter as a number : ")
    print()
    rental_days = get_integer_input("How many days will you be renting a car for? Please enter as a number : ")
    print()

    # Calling already defined functions now that there are valid inputs.

    plane = plane_cost(city_flight)
    hotel = hotel_cost(num_nights)
    car = car_rental(rental_days)

    total_holiday_cost = holiday_cost(plane, hotel, car)

    # Printing the result.

    print(f"Your plane ticket is {plane}, "
          f"your hotel stay is {hotel} and your car rental is {car},"
          f" bringing the total cost of the holiday up to {total_holiday_cost}")
    print()

    # Continuation check that allows to start another calculation if the user chooses yes. 

    continue_check = input("Would you like to make another claculation? Y/N: ").lower().strip()

    # If statement to check if the condition to break the loop is met.

    if continue_check != "y": 
        break
