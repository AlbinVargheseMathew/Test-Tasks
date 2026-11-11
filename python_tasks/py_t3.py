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

    @abstractmethod
    def calculate_discount(self, total_fare):
        pass

class BusBooking(TravelBooking):
    def __init__(self, passenger_name, number_of_tickets):
        super().__init__(passenger_name, number_of_tickets)
        self.price = 500

    def calculate_fare(self):
        return self.price * self.number_of_tickets
        # return 500

    def calculate_discount(self, total_fare):
        return total_fare * (5/100) #5% discount


    def display_booking_details(self):
        total_fare = self.calculate_fare()
        discount = self.calculate_discount(total_fare)
        final_fare = total_fare - discount

        print("\n------- BOOKING DETAILS -------\n")
        print(f"Passenger Name: {self.passenger_name}")
        print(f"Travel Type: Bus")
        print(f"Number of Tickets: {self.number_of_tickets}")
        print(f"Price Per Ticket: Rs.{self.price}")
        print(f"Original Fare: Rs.{total_fare}")
        print(f"Discount (5%): Rs.{discount}")
        print(f"Final Payable Amount: Rs.{final_fare}")
        print("\nBooking Successful!")




class TrainBooking(TravelBooking):
    def __init__(self, passenger_name, number_of_tickets):
        super().__init__(passenger_name, number_of_tickets)
        self.price = 800

    def calculate_fare(self):
        return self.price * self.number_of_tickets
        # return 800
    
    def calculate_discount(self, total_fare):
        return total_fare * (10/100)
    
    def display_booking_details(self):
        total_fare = self.calculate_fare()
        discount = self.calculate_discount(total_fare)
        final_fare = total_fare - discount

        print("\n------- BOOKING DETAILS -------\n")
        print(f"Passenger Name: {self.passenger_name}")
        print(f"Travel Type: Train")
        print(f"Number of Tickets: {self.number_of_tickets}")
        print(f"Price Per Ticket: Rs.{self.price}")
        print(f"Original Fare: Rs.{total_fare}")
        print(f"Discount (10%): Rs.{discount}")
        print(f"Final Payable Amount: Rs.{final_fare}")
        print("\nBooking Successful!")

class FlightBooking(TravelBooking):
    def __init__(self, passenger_name, number_of_tickets):
        super().__init__(passenger_name, number_of_tickets)
        self.price = 3000

    def calculate_fare(self):
        return self.price * self.number_of_tickets
        # return 3000
    
    def calculate_discount(self, total_fare):
        return total_fare * (8/100)
        
    def display_booking_details(self):
        total_fare = self.calculate_fare()
        discount = self.calculate_discount(total_fare)
        final_fare = total_fare - discount

        print("\n------- BOOKING DETAILS -------\n")
        print(f"Passenger Name: {self.passenger_name}")
        print(f"Travel Type: Flight")
        print(f"Number of Tickets: {self.number_of_tickets}")
        print(f"Price Per Ticket: Rs.{self.price}")
        print(f"Original Fare: Rs.{total_fare}")
        print(f"Discount (8%): Rs.{discount}")
        print(f"Final Payable Amount: Rs.{final_fare}")
        print("\nBooking Successful!")
    

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




    
