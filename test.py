import unittest
from calculadora import Impuestos

class calctest(unittest.TestCase):
    def test_normal_1(self):
        compra = 1000000
        porcentaje = 19

        resultado_esperado = 190000
        resultado = Impuestos.calcular(compra, porcentaje)

        self.assertEqual(round(resultado_esperado), round(resultado))
    
    def test_normal_2(self):
        compra = 200000
        porcentaje = 19

        resultado_esperado = 38000
        resultado = Impuestos.calcular(compra, porcentaje)

        self.assertEqual(round(resultado_esperado), round(resultado))
     

        
if __name__ == '__main__':
    unittest.main()