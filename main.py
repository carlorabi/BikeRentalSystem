import os
from bikeRental import BikeRental, Customer

def main():

    shop = BikeRental(20)
    customer = Customer()
    os.system('cls')
    while True:
        
        print('\n========================================================================')
        logo_banner = (
        '''
 ______      _    __                 _____      ______             _  
|_   _ \    (_)  [  |  _            / ___ `.  .' ___  |           | | 
  | |_) |   __    | | / ]   .---.  |_/___) | / .'   \_|    .--.   | | 
  |  __'.  [  |   | '' <   / /__\\  .'____.' | |   ____   / .'`\ \ | | 
 _| |__) |  | |   | |`\ \  | \__., / /_____  \ `.___]  | | \__. | |_| 
|_______/  [___] [__|  \_]  '.__.' |_______|  `._____.'   '.__.'  (_)                                              
        ''')
        print(logo_banner)
        print("""
        ============== Bike2Go! [Bike Rental Shop] =============

        [1] Display available bikes.
        \n\t[2] Rent a bike for 1 hour. = ₱50.00
        \n\t[3] Rent a bike for 1 day.  = ₱120.00
        \n\t[4] Rent a bike for 1 week. = ₱200.00
        \n\t[5] Return a bike.
        \n\t[6] Exit.
        """)
        
        choice = input("\tPlease enter your choice [1-6]: ")
        
        try:
            choice = int(choice)
        except ValueError:
            print("---------------------------------------------------------")
            print("\n\t[Error! Please input integer.]")
            print("\n---------------------------------------------------------")
            continue
        
        if choice == 1:
            shop.displaystock()
            print("\n---------------------------------------------------------")
            question = input("\n\tDo you want to continue? [yes/no]: ")
            if question=="yes":
                return main()
            elif question == "no":
                print("\n\t\t[Bye!]")
                print("----------------------------------------------------------")
                break

        elif choice == 2:
            customer.rentalTime = shop.rentBikeOnHourlyBasis(customer.requestBike())
            customer.rentalBasis = 1

        elif choice == 3:
            customer.rentalTime = shop.rentBikeOnDailyBasis(customer.requestBike())
            customer.rentalBasis = 2

        elif choice == 4:
            customer.rentalTime = shop.rentBikeOnWeeklyBasis(customer.requestBike())
            customer.rentalBasis = 3

        elif choice == 5:
            customer.bill = shop.returnBike(customer.returnBike())
            customer.rentalBasis, customer.rentalTime, customer.bikes = 0,0,0        
        elif choice == 6:
            print("\n\t\t[Thank you for renting a bike through Bike2Go!]")
            print("------------------------------------------------------------------------------")
            break
        else:
            print("---------------------------------------------------------")
            print("\n\t[Invalid input! Please enter number between 1-6.]")  
            print("\n---------------------------------------------------------")      

if __name__=="__main__":
    main()
