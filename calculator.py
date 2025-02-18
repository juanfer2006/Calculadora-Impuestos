class Taxes():
    def calculate(purchase, porcentage, Discount = 0, plastic_bag=0):
        calculate_final=(purchase - ((Discount/100)*purchase)) * (porcentage/100)
        return calculate_final
    