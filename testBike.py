import unittest
from datetime import datetime, timedelta
from bikeRental import BikeRental, Customer

class BikeRentalTest(unittest.TestCase):
    def test_Bike_Rental_diplays_correct_stock(self):
        shop1 = BikeRental()
        shop2 = BikeRental(10)
        self.assertEqual(shop1.displaystock(), 0)
        self.assertEqual(shop2.displaystock(), 10)
    def test_rentBikeOnHourlyBasis_for_negative_number_of_bikes(self):
        shop = BikeRental(10)
        self.assertEqual(shop.rentBikeOnHourlyBasis(-1), None)
    def test_rentBikeOnHourlyBasis_for_zero_number_of_bikes(self):
        shop = BikeRental(10)
        self.assertEqual(shop.rentBikeOnHourlyBasis(0), None)
    def test_rentBikeOnHourlyBasis_for_valid_positive_number_of_bikes(self):
        shop = BikeRental(10)
        hour = datetime.now().hour
        self.assertEqual(shop.rentBikeOnHourlyBasis(2).hour, hour)
    def test_rentBikeOnHourlyBasis_for_invalid_positive_number_of_bikes(self):
        shop = BikeRental(10)
        self.assertEqual(shop.rentBikeOnHourlyBasis(11), None)
    def test_rentBikeOnDailyBasis_for_negative_number_of_bikes(self):
        shop = BikeRental(10)
        self.assertEqual(shop.rentBikeOnDailyBasis(-1), None)
    def test_rentBikeOnDailyBasis_for_zero_number_of_bikes(self):
        shop = BikeRental(10)
        self.assertEqual(shop.rentBikeOnDailyBasis(0), None)
    def test_rentBikeOnDailyBasis_for_valid_positive_number_of_bikes(self):
        shop = BikeRental(10)
        hour = datetime.now().hour
        self.assertEqual(shop.rentBikeOnDailyBasis(2).hour, hour)
    def test_rentBikeOnDailyBasis_for_invalid_positive_number_of_bikes(self):
        shop = BikeRental(10)
        self.assertEqual(shop.rentBikeOnDailyBasis(11), None)
     
    def test_rentBikeOnWeeklyBasis_for_negative_number_of_bikes(self):
        shop = BikeRental(10)
        self.assertEqual(shop.rentBikeOnWeeklyBasis(-1), None)
    def test_rentBikeOnWeeklyBasis_for_zero_number_of_bikes(self):
        shop = BikeRental(10)
        self.assertEqual(shop.rentBikeOnWeeklyBasis(0), None)
    def test_rentBikeOnWeeklyBasis_for_valid_positive_number_of_bikes(self):
        shop = BikeRental(10)
        hour = datetime.now().hour
        self.assertEqual(shop.rentBikeOnWeeklyBasis(2).hour, hour)
    def test_rentBikeOnWeeklyBasis_for_invalid_positive_number_of_bikes(self):
        shop = BikeRental(10)
        self.assertEqual(shop.rentBikeOnWeeklyBasis(11), None)
    
    def test_returnBike_for_invalid_rentalTime(self):
        # create a shop and a customer
        shop = BikeRental(10)
        customer = Customer()

        # let the customer not rent a bike a try to return one.
        request = customer.returnBike()
        self.assertIsNone(shop.returnBike(request))

        # manually check return function with error values
        self.assertIsNone(shop.returnBike((0,0,0)))
