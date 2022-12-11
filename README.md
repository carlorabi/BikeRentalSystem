# Bike Rental System

1. A full fledged bike rental system implemented in Python using object oriented programming.
2. Customers can see available bikes on the shop Rent bikes on hourly basis ₱50 per 1 hour.Rent bikes on daily basis ₱120 per 1 day.Rent bikes on weekly basis ₱200 per 1 week. The rental shops can issue a bill when customer decides to return the bike, display available inventory take requests on hourly, daily and weekly basis by cross verifying stockSince classes are used various customers and bike rental shops can be instantiated as needed.
3. For simplicity we assume that any customer requests rentals of only one type i.e hourly, monthly or weekly but is free to chose the number of bikes he/she wants. However requested bikes should be less than available stock.

# Unit-Test
To thoroughly check the classes and methods for faults, a test module is developed alongside the main software. The majority of mistakes are caused by non-integer inputs, negative values, and null values. The majority of them have been looked after.

# Running the tests
To run the tests, run the appropriate command below (why they are different):
Python 2.7: py.test bikeRental_test.py
Python 3.4+: pytest bikeRental_test.py

Alternatively, you can tell Python to run the pytest module (allowing the same command to be used regardle ss of Python version): python -m pytest bikeRental_test.py

# Scope of the project 
This undertaking outlines the thoughts and techniques for composing programs in pythons utilizing loop concept and using OOP concepts.


# Stepwise algorithm
- Step 1:	  Start
- Step 2:	  Displaying main menu.
- Step 3:   When the user press 1, Menu is displayed in the screen with the numbers of bikes available in the store.
- Step 4:	  And it will ask a user if he/she want to continue (yes/no).
- Step 5:   If the user choose yes, it will continue otherwise the program will be terminated or stop.
- Step 6:   When the user press 2, 3, 4 it will display the number of bikes he/she want.
- Step 7:   If the user input string it will loop  and ask again the quantity of bikes that customer want.
- Step 8:   When the user press 5, it will show the bill of the customer. 1 hour (quantity of bikes * 50) 1 day (quantity of bikes * 120) 1 week (quantity of bikes * 200)
- Step 13:	 End.


# Screenshots of the Program

<img width="572" alt="Screenshot1" src="https://user-images.githubusercontent.com/113867873/206838092-6a8e4226-01c9-44ef-aef6-b928036f43d2.png">

<img width="530" alt="Screenshot2" src="https://user-images.githubusercontent.com/113867873/206838133-98df10dd-6845-41f0-ba3b-05da0c4dd138.png">

<img width="538" alt="Screenshot3" src="https://user-images.githubusercontent.com/113867873/206838183-06f61158-c27e-4158-bf8a-e1967193b833.png">

<img width="436" alt="Screenshot4" src="https://user-images.githubusercontent.com/113867873/206838246-929a64c8-c368-4f17-805e-443662159e83.png">


# UML Diagram
![UML_Diagram](https://user-images.githubusercontent.com/113867873/206898976-4f59f8f0-de0b-4cc2-9dd5-33961853cfe3.jpg)


# Video Presentation
Link: 


# Authors
* Rabi, John Carlo (@carlorabi)
* Cachero, Angelica Marie (@angelicachero)
* Castillo, Cyrus Alexis (@cyruscastillo)
* Macuha, Bien Joshua (@bienjoshuaa)
