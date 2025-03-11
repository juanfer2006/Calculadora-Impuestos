class ErrorValueNegative(Exception):
    def __init__(self, purchase):
        super().__init__(f'No se pude calcular el impuesto. El valor {purchase} no es valido. Ingrese un valor mayor a 0')

class ErrorIncorrectIVA(Exception):
    def __init__(self, porcentage):
        super().__init__(f'No se pude calcular el impuesto. El porcentaje de IVA {porcentage} no es valido. Ingrese uno de los siguientes valorea: 0, 5, 19')
 
class ErrorDiscount(Exception):
    def __init__(self, discount):
        super().__init__(f'No se pude calcular el impuesto. El valor {discount} no es valido. Ingrese un valor menor a 100')

class ErrorStringIva(Exception):
    ...

class ErrorPorcentage(Exception):
    ...

class Taxes():
    def calculate(purchase, porcentage, discount=0, plastic_bag=0, currency='COP'):
        dollar_value = 4500
        plastic_bag_tax = 65
        
        if type(purchase) == str:
            raise ErrorStringIva()

        if type(porcentage) == str:
            raise ErrorPorcentage()

        if purchase <= 0:
            raise ErrorValueNegative(purchase)

        if porcentage != 19 and porcentage != 5 and porcentage != 0:
            raise ErrorIncorrectIVA(porcentage)
        
        if discount > 100:
           raise ErrorDiscount(discount)

        if currency == 'USD':
            purchase = purchase * dollar_value

        calculate_final = (purchase - ((discount/100)*purchase)) * (porcentage/100)
        calculate_final2 = calculate_final + (plastic_bag * plastic_bag_tax)

        return calculate_final2
    