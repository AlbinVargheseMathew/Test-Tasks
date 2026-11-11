# online travelling booking  system
from abc import ABC, abstractmethod

class TravelBooking(ABC):
    def __init__(self, passenger_name, number_of_tickets):
        self.passenger_name = passenger_name
        self.number_of_tickets = number_of_tickets
        # self.total = total

    @abstractmethod
    def calculate_fare(self):
        pass

    @abstractmethod
    def display_booking_details(self):
        pass

    # @abstractmethod
    # def calculate_discount(self):
    #     pass

class BusBooking(TravelBooking):
    def __init__(self, passenger_name, number_of_tickets):
        super().__init__(passenger_name, number_of_tickets)
        self.price = 500

    def calculate_fare(self, total):
        self.total = total
        self.total = self.price * self.number_of_tickets

    def display_booking_details(self):
        print("Bus Booking Details")
        print("Passenger Name: ",self.passenger_name)
        print("Number of Tickets: ",self.number_of_tickets)
        print("Price Per Ticket: Rs.",self.price)
        print("Total fare: Rs.", self.total )

class TrainBooking(TravelBooking):
    def __init__(self, passenger_name, number_of_tickets):
        super().__init__(passenger_name, number_of_tickets)
        self.price = 800

    def calculate_fare(self):
        self.total = self.price * self.number_of_tickets
    
    def display_booking_details(self):
        print("Train Booking Details")
        print("Passenger Name: ",self.passenger_name)
        print("Number of Tickets: ",self.number_of_tickets)
        print("Price Per Ticket: Rs.",self.price)
        print("Total fare: Rs.", self.total )

class FlightBooking(TravelBooking):
    def __init__(self, passenger_name, number_of_tickets):
        super().__init__(passenger_name, number_of_tickets)
        self.price = 3000

    def calculate_fare(self):
        self.total = self.price * self.number_of_tickets
        
    def display_booking_details(self):
        print("Flight Booking Details")
        print("Passenger Name: ",self.passenger_name)
        print("Number of Tickets: ",self.number_of_tickets)
        print("Price Per Ticket: Rs.",self.price)
        print("Total fare: Rs.", self.total )
    

print("WELCOME TO TRAVEL BOOKING SYSTEM \n")
passenger_name = input("Enter Passenger Name: ")
number_of_tickets = int(input("Enter Number of Tickets: "))
print("\n")
print("Available Booking Options: \n")
print("""
1. Bus
2. Train
3. Flight
\n """)

choice = int(input("Select Your Booking: "))
# print(" \n ------- BOOKING DETAILS ------- \n")

if choice == 1:
    booking = BusBooking(passenger_name,number_of_tickets)
elif choice == 2:
    booking = TrainBooking(passenger_name, number_of_tickets)
elif choice == 3:
    booking = FlightBooking(passenger_name,number_of_tickets)
else:
    print("Invalid Choice")
    exit()

print(" \n ------- BOOKING DETAILS ------- \n")
booking.display_booking_details()




    
