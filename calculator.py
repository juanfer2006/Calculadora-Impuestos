class Taxes():
    def calculate(purchase, porcentage, Discount = 0, plastic_bag=0, currency='COP'):
        if currency == 'USD':
            purchase = purchase * 4500
        calculate_final=(purchase - ((Discount/100)*purchase)) * (porcentage/100)
        calculate_final2 = calculate_final + (plastic_bag * 65)
        return calculate_final2
    