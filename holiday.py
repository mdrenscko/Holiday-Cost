#Initialize variables
num_nights = int(input("Enter the number of nights you will be staying at a hotel: "))
city_flight = ["London", "Paris", "New York", "San Francisco", "Gibraltar"] #City destination
rental_days = int(input( "Enter the number of days for which you will be hiring a car: "))
cost = [200, 250, 600, 700, 300] #Flight cost for the cities listed in the order above (dictionary is not callable)



#Define functions
price_per_night = 100 #price per night charged at the hotel
def hotel_cost(num_nights):
    y = num_nights * price_per_night
    return y
print("HotelCost:")
nights_hotel = hotel_cost(num_nights) #hotel cost for the required number of nights
print(nights_hotel)

city = input("Enter a city from the list: ")
if city in city_flight:
    print(city)
else: 
    print("City not available")

def plane_cost(city):
    for city in city_flight:
       y = city
       return y
print("Plane Cost:")
index = city_flight.index(city)
plane = cost[index]
print(plane)  

daily_rental_cost = 100
def car_rental(rental_days):
    y = rental_days * daily_rental_cost
    return y
print("Car Rental Cost:")
car_days= car_rental(rental_days) #car rental cost for the required number of days
print(car_days)

def holiday_cost(hotel, plane, car):
    y = hotel + plane + car
    return y
print("Total Holiday Cost:")
sum = holiday_cost(nights_hotel, plane, car_days)
print(sum)
   
    
        