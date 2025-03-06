import sys
sys.path.append('src')
from model.calculator import *

try:
    purchase = float(input("Ingrese el valor la compra: "))
    porcentage = float(input('Ingrese el porcentaje de IVA: '))
    discount = float(input("Ingrese el descuento: "))
    plastic_bag = float(input("Ingrese la cantidad de bolsas plasticas: "))
    currency = str(input("Ingrese una moneda valida: USD o COP: "))

    calculation = Taxes.calculate(purchase, porcentage, discount, plastic_bag, currency)
    print(f"El valor de la cuota es: {calculation}")
except ValueError as err:
    print('Formato incorrecto')
except Exception as err:
    print(f"Ocurrio un error: { err }")