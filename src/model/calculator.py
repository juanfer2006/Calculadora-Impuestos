class ErrorValueNegative(Exception):
    """ 
    Exception to indicate that the comparison value is negative
    
    Excepcion para indicar que el valor de la compara es negativo
    """
    def __init__(self, purchase):
        """ 
        To use this exception, you must call the constructor indicating the purchase value.
    
        Para usar esta excepción, debe llamar al constructor indicando el valor de la compra
        """
        super().__init__(f'No se pude calcular el impuesto. El valor {purchase} no es valido. Ingrese un valor mayor a 0')

class ErrorIncorrectIVA(Exception):
    """ 
    Exception to indicate that the IVA value is incorrect
    
    Excepcion para indicar que el valor de el IVA es incorrecto
    """
    def __init__(self, porcentage):
        """ 
        To use this exception, you must call the constructor indicating the IVA value.
    
        Para usar esta excepción, debe llamar al constructor indicando el valor de el IVA
        """
        super().__init__(f'No se pude calcular el impuesto. El porcentaje de IVA {porcentage} no es valido. Ingrese uno de los siguientes valorea: 0, 5, 19')
 
class ErrorDiscount(Exception):
    """
    Exception to indicate that the discount value exceeds 100% of the purchase
    
    Excepcion para indicar que el valor de el descuenta supera el 100% de la compra
    """
    def __init__(self, discount):
        """ 
        To use this exception, you must call the constructor indicating the value of the discount
    
        Para usar esta excepción, debe llamar al constructor indicando el valor de el descuento
        """
        super().__init__(f'No se pude calcular el impuesto. El valor de descuento {discount} no es valido. Ingrese un valor menor a 100')

class ErrorStringIva(Exception):
    """ 
    Exception to indicate that the IVA data type is incorrect, it must be a positive integer
    
    Excepcion para indicar que el tipo de dato del IVA es incorrecto, debe ser un entero positivo
    """
    ...

class ErrorPorcentage(Exception):
    """ 
    Exception to indicate that the percentage data type is incorrect, it must be a positive integer
    
    Excepcion para indicar que el tipo de dato del porcentaje es incorrecto, debe ser un entero positivo
    """
    ...

class Taxes():
    """
    Class to obtain the IVA payable on a purchase

    Clase para obtener el IVA a pagar de una compra
    """
    def calculate(purchase, porcentage, discount=0, plastic_bag=0, currency='COP'):
        """
        Calculate the VAT payable on a purchase

        Calcula el IVA a pagar de una compra
        """
        #Para efectos de calular el IVA con dolar, se hace el cambio de moneda
        dollar_value = 4500 
        #Para calcular el IVA se tiene encuenta el impuesto que tiene las bolsas plasticas
        plastic_bag_tax = 65 
        
        if type(purchase) == str:
            """
            If the purchase is of type str, it throws an ErrorStringIVA exception.
            Si la compra es de tipo str, arroja una excepcion ErrorStringIVA
            """
            raise ErrorStringIva()

        if type(porcentage) == str:
            """
            If the IVA is of type str, it throws an ErrorPercentage exception.
            Si el IVA es de tipo str, arroja una excepcion ErrorPorcentage
            """
            raise ErrorPorcentage()

        if purchase <= 0:
            """
            If the purchase is less than or equal to 0, throws an ErrorValueNegative exception
            Si la compra es menor o igual a 0, arroja una excepcion ErrorValueNegative
            """
            raise ErrorValueNegative(purchase)

        if porcentage != 19 and porcentage != 5 and porcentage != 0:
            """
            If the IVA value is different from 19.5 or 0, an ErrorIncorrectIVA exception is thrown.
            Si el valor del IVA es diferente de 19,5 o 0, arroja una excepcion ErrorIncorrectIVA
            """
            raise ErrorIncorrectIVA(porcentage)
        
        if discount > 100:
            """
            If the discount value exceeds 100%, an ErrorDiscount exception is thrown.
            Si el valor del descuento supera el 100%, arroja una excepcion ErrorDiscount
            """
            raise ErrorDiscount(discount)

        if currency == 'USD':
            """
            If the currency type is dollar, change the value to Colombian pesos
            Si el tipo de moneda es dolar cambia el valor a pesos colombianos
            """
            purchase = purchase * dollar_value

        calculate_final = (purchase - ((discount/100)*purchase)) * (porcentage/100)
        """
        The IVA to be paid is calculated and then the tax on plastic bags is added.
        Se calcula el IVA a pagar y despues se le suma el impuesto de las bolsas de plasticos
        """
        calculate_final2 = calculate_final + (plastic_bag * plastic_bag_tax)

        return calculate_final2
    