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

    def setUpClass():
        CalculatorController.delete_table()
        CalculatorController.create_table()

    def test_insert_DB_1(self):
        user = User(id = '12', name = 'David')
        CalculatorController.insert(user)
        date_sought = CalculatorController.search('12')
        self.assertTrue(date_sought.is_equal(user))

    def test_insert_tax_DB_1(self):
        user_id = '12'
        purchase = 1000000
        porcentage = 19
        discount = 0
        plastic_bags = 0
        currency = 'COP'
        
        tax_value = Taxes.calculate(purchase, porcentage, discount, plastic_bags, currency)
        tax = TaxRecord(
            user_id=user_id,
            purchase=purchase,
            porcentage=porcentage,
            discount=discount,
            plastic_bags=plastic_bags,
            currency=currency,
            tax_value=tax_value
        )

        # No lanza error si se inserta correctamente
        CalculatorController.insert_tax(tax)

    def test_update_tax_DB_1(self):
        user_id = '12'
        # Ahora hacemos la actualización
        new_purchase = 2000000
        new_porcentage = 19
        new_discount = 5
        new_plastic_bags = 2
        new_currency = 'COP'

        new_tax_value = Taxes.calculate(
            new_purchase, new_porcentage, new_discount, new_plastic_bags, new_currency
        )
        updated_tax = TaxRecord(
            user_id=user_id,
            purchase=new_purchase,
            porcentage=new_porcentage,
            discount=new_discount,
            plastic_bags=new_plastic_bags,
            currency=new_currency,
            tax_value=new_tax_value
        )

        CalculatorController.update_tax(updated_tax)

        # Verificamos la actualización
        cursor = CalculatorController.GetCursor()
        cursor.execute(f"SELECT purchase, porcentage, discount, plastic_bags, currency, tax_value FROM taxes WHERE user_id = '{user_id}'")
        fila = cursor.fetchone()
        
        self.assertEqual(fila, (
            new_purchase, new_porcentage, new_discount,
            new_plastic_bags, new_currency, new_tax_value
        ))

    def test_delete_tax_DB_1(self):
        user = User(id='12', name='David') # Insertamos usuario primero
        # Ahora borramos el impuesto
        CalculatorController.delete_tax(user.id)
        # Verificamos que ya no exista
        cursor = CalculatorController.GetCursor()
        cursor.execute(f"SELECT * FROM taxes WHERE user_id = '{user.id}'")
        fila = cursor.fetchone()

        self.assertIsNone(fila)



        
if __name__ == '__main__':
    unittest.main()