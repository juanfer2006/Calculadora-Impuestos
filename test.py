import unittest
from calculator import Taxes

class calctest(unittest.TestCase):
    def test_normal_1(self):
        purchase = 1000000
        porcentage = 19

        expected_result = 190000
        result = Taxes.calculate(purchase, porcentage)

        self.assertEqual(round(expected_result), round(result))
    
    def test_normal_2(self):
        purchase = 200000
        porcentage = 19

        expected_result = 38000
        result = Taxes.calculate(purchase, porcentage)

        self.assertEqual(round(expected_result), round(result))

    def test_normal_3(self):
        pass

        
if __name__ == '__main__':
    unittest.main()