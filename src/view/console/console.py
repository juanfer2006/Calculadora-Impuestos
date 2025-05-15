import sys
sys.path.append('src')
from model.calculator import *
from controller.calculator_controller import *

try:
    user_id = input("Ingrese su ID de usuario: ")

    purchase = float(input("Ingrese el valor la compra: "))
    porcentage = float(input('Ingrese el porcentaje de IVA: '))
    discount = float(input("Ingrese el descuento: "))
    plastic_bag = float(input("Ingrese la cantidad de bolsas plasticas: "))
    currency = str(input("Ingrese una moneda valida: USD o COP: "))

    calculation = Taxes.calculate(purchase, porcentage, discount, plastic_bag, currency)
    print(f"El valor de la cuota es: {calculation}")

    # Funcionalidad en la Interfaz de Usuario para Insertar Datos
    tax = TaxRecord(
        user_id=user_id,
        purchase=purchase,
        porcentage=porcentage,
        discount=discount,
        plastic_bags=plastic_bag,
        currency=currency,
        tax_value=calculation
    )

    CalculatorController.insert_tax(tax)
    print("Registro insertado correctamente en la base de datos.")

    # Funcionalidad en la Interfaz de Usuario para Modificar Datos
    modificar = input("¿Desea modificar este registro? (s/n): ").lower()
    if modificar == 's':
        new_purchase = float(input("Ingrese el nuevo valor de la compra: "))
        new_porcentage = float(input("Ingrese el nuevo porcentaje de IVA: "))
        new_discount = float(input("Ingrese el nuevo descuento: "))
        new_plastic_bags = float(input("Ingrese la nueva cantidad de bolsas plásticas: "))
        new_currency = str(input("Ingrese la nueva moneda válida: USD o COP: "))

        new_tax_value = Taxes.calculate(new_purchase, new_porcentage, new_discount, new_plastic_bags, new_currency)
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
        print("Registro actualizado correctamente en la base de datos.")

except ValueError:
    print('Formato incorrecto')

except Exception as err:
    print(f"Ocurrió un error: {err}")
