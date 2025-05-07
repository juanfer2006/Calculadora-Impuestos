import unittest
import sys
sys.path.append('src')
sys.path.append( "." )
from model.calculator import *
from controller.calculator_controller import CalculatorController

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
        purchase = 1500000
        porcentage = 19
        discount = 10

        expected_result = 256500
        result = Taxes.calculate(purchase, porcentage, discount)

        self.assertEqual(round(expected_result), round(result))

    def test_extraordinary_1(self):
        purchase = 500000
        porcentage = 0

        expected_result = 0
        result = Taxes.calculate(purchase, porcentage)

        self.assertEqual(round(expected_result), round(result))

    def test_extraordinary_2(self):
        purchase = 1200
        porcentage = 19
        currency = 'USD'

        expected_result = 1026000
        result = Taxes.calculate(purchase, porcentage, currency=currency)

        self.assertEqual(round(expected_result), round(result))

    def test_extraordinary_3(self):
        purchase = 150000
        porcentage = 19
        plastic_bag = 3

        expected_result = 28695
        result = Taxes.calculate(purchase, porcentage, plastic_bag=plastic_bag)

        self.assertEqual(round(expected_result), round(result))
        
    def test_error_1(self):
        purchase = -1000000
        porcentage = 19
        
        with self.assertRaises(ErrorValueNegative):
            Taxes.calculate(purchase, porcentage)
            
    def test_error_2(self):
        purchase = 1000000
        porcentage = 150
        
        with self.assertRaises(ErrorIncorrectIVA):
            Taxes.calculate(purchase, porcentage)
            
    def test_error_3(self):
        purchase = 'Un millón de pesos'
        porcentage = 19
        
        with self.assertRaises(ErrorStringIva):
            Taxes.calculate(purchase, porcentage)

    def test_error_4(self):
        purchase = 1000000
        porcentage = 'Diecinueve%'
        
        with self.assertRaises(ErrorPorcentage):
            Taxes.calculate(purchase, porcentage)

    def test_insertar_DB(self):
        user = User(id = '12', name = 'David')
        CalculatorController.insert(user)
        dato_buscado = CalculatorController.search('12')
        self.assertTrue(dato_buscado.is_equal(user))
        
if __name__ == '__main__':
    unittest.main()