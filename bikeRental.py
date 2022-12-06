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
