import datetime

class BikeRental:
    
    def __init__(self,stock = 0):
        """
        Our constructor class that instantiates bike rental shop.
        """
        self.stock = stock 
    def displaystock(self):
        #Displays the bikes currently available for rent in the shop.
        print("---------------------------------------------------------")
        print("\n\t[We have currently {} bikes available to rent.]".format(self.stock))
        return self.stock
        
         def rentBikeOnHourlyBasis(self, n):
        #Rents a bike on hourly basis to a customer.
     
        if n <= 0:
            print("\n\t\t[Quantity of bikes should be positive!]") # reject invalid input
            return None

        elif n > self.stock:
            print("---------------------------------------------------------")
            print("\n\tSorry! We only have {} bikes available to rent.".format(self.stock)) # do not rent bike when stock is less than requested bikes.
            print("\n---------------------------------------------------------")
            return None
                
        else:
            now = datetime.datetime.now()                      
            print("\nYou have rented a {} bike(s) on hourly basis today at {} hours.".format(n,now.hour))
            print("\nYou will be charged ₱50.00 for each hour per bike. We hope that you enjoy our service!")
            self.stock -= n
            return now 

       def rentBikeOnDailyBasis(self, n):
        """
        Rents a bike on daily basis to a customer.
        """
        if n <= 0:
            print("Number of bikes should be positive!")
            return None

        elif n > self.stock:
            print("Sorry! We have currently {} bikes available to rent.".format(self.stock))
            return None
    
        else:
            now = datetime.datetime.now()                      
            print("You have rented {} bike(s) on daily basis today at {} hours.".format(n, now.hour))
            print("You will be charged $20 for each day per bike.")
            print("We hope that you enjoy our service.")

            self.stock -= n
            return now        

         def rentBikeOnWeeklyBasis(self, n):
        #Rents a bike on weekly basis to a customer.
    
        if n <= 0:
            print("Number of bikes should be positive!")
            return None
        elif n > self.stock:
            print("Sorry! We have currently {} bikes available to rent.".format(self.stock))
            return None        
        
        else:
            now = datetime.datetime.now()
            print("\n\tYou have rented {} bike(s) on weekly basis today at {} hours.".format(n, now.hour))
            print("\n\tYou will be charged ₱200.00 for each week per bike. We hope that you enjoy our service!")
            self.stock -= n
            return now
       
       def returnBike(self, request):
        """
        1. Accept a rented bike from a customer
        2. Inventory updated
        3. Return a bill
        """
       
        # extract the tuple and initiate bill
        rentalTime, rentalBasis, numOfBikes = request
        bill = 0

        # issue a bill only if all three parameters are not null!
        if rentalTime and rentalBasis and numOfBikes:
            self.stock += numOfBikes
            now = datetime.datetime.now()
            rentalPeriod = now - rentalTime
        
            # hourly bill calculation
            if rentalBasis == 1:
                bill = round(rentalPeriod.seconds / 3600) * 50 * numOfBikes
                
            # daily bill calculation
            elif rentalBasis == 2:
                bill = round(rentalPeriod.days) * 120 * numOfBikes
                
            # weekly bill calculation
            elif rentalBasis == 3:
                bill = round(rentalPeriod.days / 7) * 200 * numOfBikes
            
            print("\n\tThat would be ₱{}.00".format(bill))
            print("\n\t[Thank you!]")
            return bill
        
        else:
            print("---------------------------------------------------------")
            print("\n\tYou are not renting any bikes from Bike2Go!")
            print("\n---------------------------------------------------------") 
            return None
          
class Customer:

    def __init__(self):
        """
        Our constructor method which instantiates various customer objects.
        """
        
        self.bikes = 0
        self.rentalBasis = 0
        self.rentalTime = 0
        self.bill = 0

    
    def requestBike(self):
        """
        Takes a request from the customer for the number of bikes.
        """
                      
        bikes = input("How many bikes would you like to rent?")
        try:
            bikes = int(bikes)
        except ValueError:
            print("That's not a positive integer!")
            return -1

        if bikes < 1:
            print("Invalid input. Number of bikes should be greater than zero!")
            return -1
        else:
            self.bikes = bikes
        return self.bikes
     
    def returnBike(self):
        """
        Allows customers to return their bikes to the rental shop.
        """
        if self.rentalBasis and self.rentalTime and self.bikes:
            return self.rentalTime, self.rentalBasis, self.bikes  
        else:
            return 0,0,0
