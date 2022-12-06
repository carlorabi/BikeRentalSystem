import unittest
from datetime import datetime, timedelta
from bikeRental import BikeRental, Customer

class BikeRentalTest(unittest.TestCase):
    def test_Bike_Rental_diplays_correct_stock(self):
        shop1 = BikeRental()
        shop2 = BikeRental(10)
        self.assertEqual(shop1.displaystock(), 0)
        self.assertEqual(shop2.displaystock(), 10)
