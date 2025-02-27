from calculator import Taxes

purchase = input("Ingrese el valor la compra: ")
porcentage = float(input('Ingrese el porcentaje de IVA: '))
Discount = float(input("Ingrese el descuento:"))
plastic_bag = float(input("Ingrese la cantidad de bolsas plasticas: "))
currency = str(input("Ingrese una moneda valida: USD o COP: "))

try:
    calculation = Taxes.calculate(purchase, porcentage, Discount, plastic_bag, currency)
    print(f"El valor de la cuota es: {calculation}")
except Exception as err:
    print(f"Ocurrio un error: { err }")