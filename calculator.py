class ErrorValueNegative(Exception):
    def __init__(self):
        super().__init__(f'NOOOOO')

class ErrorIncorrectIVA(Exception):
    ...

class ErrorStringIva(Exception):
    ...

class ErrorPorcentage(Exception):
    ...

class Taxes():
    def calculate(purchase, porcentage, discount=0, plastic_bag=0, currency='COP'):
        if type(purchase) == str:
            raise ErrorStringIva()

        if type(porcentage) == str:
            raise ErrorPorcentage()

        if purchase < 0:
            raise ErrorValueNegative()

        if porcentage != 19 and porcentage != 5 and porcentage != 0:
            raise ErrorIncorrectIVA()

        if currency == 'USD':
            purchase = purchase * 4500

        calculate_final = (purchase - ((discount/100)*purchase)) * (porcentage/100)
        calculate_final2 = calculate_final + (plastic_bag*65)

        return calculate_final2
    