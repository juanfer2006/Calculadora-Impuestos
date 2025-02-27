class ErrorValueNegative(Exception):
    def __init__(self, purchase):
        super().__init__(f'No se pude calcular el impuesto. El valor {purchase} es negativo. Ingrese un valor positivo')

class ErrorIncorrectIVA(Exception):
    def __init__(self, porcentage):
        super().__init__(f'No se pude calcular el impuesto. El porcentaje de IVA {porcentage} no es valido. Ingrese uno de los siguientes valorea: 0, 5, 19')
 

class ErrorStringIva(Exception):
    def __init__(self, purchase):
        super().__init__(f'No se pude calcular el impuesto.')

class ErrorPorcentage(Exception):
    ...

class Taxes():
    def calculate(purchase, porcentage, discount=0, plastic_bag=0, currency='COP'):
        if type(purchase) == str:
            raise ErrorStringIva()

        if type(porcentage) == str:
            raise ErrorPorcentage()

        if purchase < 0:
            raise ErrorValueNegative(purchase)

        if porcentage != 19 and porcentage != 5 and porcentage != 0:
            raise ErrorIncorrectIVA(porcentage)

        if currency == 'USD':
            purchase = purchase * 4500

        calculate_final = (purchase - ((discount/100)*purchase)) * (porcentage/100)
        calculate_final2 = calculate_final + (plastic_bag*65)

        return calculate_final2
    