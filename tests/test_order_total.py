import unittest
 
from app.order_total import order_total
 
 
class OrderTotalTests(unittest.TestCase):
    def test_single_item(self):
        self.assertEqual(order_total(350, 1), 350)
 
    def test_dozen_gets_discount(self):
        self.assertEqual(order_total(200, 12), 2160)
 
    def test_zero_items_is_refused(self):
        with self.assertRaises(ValueError):
            order_total(200, 0)
