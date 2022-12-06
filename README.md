# Bike Rental System

1. A full fledged bike rental system implemented in Python using object oriented programming.
2. Customers can see available bikes on the shop Rent bikes on hourly basis $5 per hour.Rent bikes on daily basis $20 per day.Rent bikes on weekly basis $60 per week. Family Rental, a promotion that can include from 3 to 5 Rentals (of any type) with a discount of 30% of the total priceThe rental shops canissue a bill when customer decides to return the bike, display available inventorytake requests on hourly, daily and weekly basis by cross verifying stockSince classes are used various customers and bike rental shops can be instantiated as needed.
3. For simplicity we assume that any customer requests rentals of only one type i.e hourly, monthly or weekly but is free to chose the number of bikes he/she wants. However requested bikes should be less than available stock.

# Unit-Test
To thoroughly check the classes and methods for faults, a test module is developed alongside the main software. The majority of mistakes are caused by non-integer inputs, negative values, and null values. The majority of them have been looked after.

# Running the tests
To run the tests, run the appropriate command below (why they are different):
Python 2.7: py.test bikeRental_test.py
Python 3.4+: pytest bikeRental_test.py

Alternatively, you can tell Python to run the pytest module (allowing the same command to be used regardle ss of Python version): python -m pytest bikeRental_test.py

# Scope of the project 
This undertaking outlines the thoughts and techniques for composing programs in pythons utilizing loop concept. It additionally comprises algorithm, pseudocode, flowchart and data structure of the program. therefore, this undertaking will be extremely useful for every one of those understudies, programmer, software engineers and python learner students to discover how the code execute and work in the program. Similarly, It will instruct the strategy of different data structure which has been utilized as a part of the program. At last, as the program is composed with great clarification in each progression so it will help every one of those students who discover trouble in python.


# Stepwise algorithm
- Step 1:	  Start 
- Step 2:	  products.txt file from given folder.
- Step 3:   txt file is displayed in the screen with products available.
- Step 4:	  Inputs customers name.
- Step 5: 	Inputs products name.
- Step 6: 	If product name is correct then go to next step or else remain in same step until valid name is provided.
- Step 7: 	Input quantity of the product.
- Step 8: 	If the input number of quantity is available then go to next step or else display Sorry!! a_name !, product is out of stock.
- Step 9: 	Ask customer do you want buy more products?(Y/N) If they select Y, go back to step 6, If they select no, then it won’t go to any steps.
- Step 10: 	Price of the product with total amount is displayed.
- Step 11:	Receipt is printed with customer name, date and time purchase. Products details, Grand total and at last Thank You customer for buying Let's Dough It! Pizza. See you again!
- Step 12: 	If more customers are there to purchase item ‘Y’ should be clicked and go to step or else end.
- Step 13:	 End.
