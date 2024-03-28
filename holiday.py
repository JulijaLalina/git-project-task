while True:
   
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

    city_flight = input("Which city are you going to? : ").lower().strip()
    print()

    while city_flight not in flight_price:
        print("Sorry we do not have flight price information for this destination.")
        city_flight = input("Choose another? : ").lower().strip()
        print()

    num_nights = int(input("How many nights are you staying? Please enter as a number : "))
    print()
    rental_days = int(input("How many days will you be renting a car for? Please enter as a number : "))
    print()

    def plane_cost(city_flight):
        ticket_price = flight_price[city_flight]
        return ticket_price

    def hotel_cost(num_nights):
        hotel_rate = 100
        hotel_price = hotel_rate * num_nights
        return hotel_price

    def car_rental(rental_days):
        rate = 50
        rental_cost = rental_days * rate
        return rental_cost

    plane = plane_cost(city_flight)
    hotel = hotel_cost(num_nights)
    car = car_rental(rental_days)

    def holiday_cost(plane, hotel, car):
        total_holiday_cost = plane + hotel + car
        return total_holiday_cost

    total_holiday_cost = holiday_cost(plane, hotel, car)

    print(f"Your plane ticket is {plane}, "
          f"your hotel stay is {hotel} and your car rental is {car},"
          f" bringing the total cost of the holiday up to {total_holiday_cost}")
    print()
  
    continue_check = input("Would you like to make another claculation? Y/N: ").lower().strip()

    if continue_check != "y":
        break
