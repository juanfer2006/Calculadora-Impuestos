import sys
sys.path.append('src')

from model.calculator import Taxes, User, TaxRecord
from model import db
from model.db_models import User as DBUser, TaxRecord as DBTax

class CalculatorController:

    @staticmethod
    def create_table():
        db.create_all()

    @staticmethod
    def delete_table():
        db.drop_all()

    @staticmethod
    def insert(user: User):
        nuevo_usuario = DBUser(id=user.id, name=user.name)
        db.session.add(nuevo_usuario)
        db.session.commit()

    @staticmethod
    def insert_tax(tax: TaxRecord):
        tax_value = Taxes.calculate(
            purchase=tax.purchase,
            porcentage=tax.porcentage,
            discount=tax.discount,
            plastic_bag=tax.plastic_bags,
            currency=tax.currency
        )
        tax.tax_value = tax_value

        nueva_compra = DBTax(
            user_id=tax.user_id,
            purchase=tax.purchase,
            porcentage=tax.porcentage,
            discount=tax.discount,
            plastic_bags=tax.plastic_bags,
            currency=tax.currency,
            tax_value=tax.tax_value
        )
        db.session.add(nueva_compra)
        db.session.commit()
        return True

    @staticmethod
    def search(id: str):
        user = DBUser.query.filter_by(id=id).first()
        if not user:
            return None

        compras_db = DBTax.query.filter_by(user_id=id).all()
        compras = [
            {
                'id': compra.id,
                'purchase': compra.purchase,
                'porcentage': compra.porcentage,
                'discount': compra.discount,
                'plastic_bags': compra.plastic_bags,
                'currency': compra.currency,
                'tax_value': compra.tax_value
            }
            for compra in compras_db
        ]

        return {'user': User(user.id, user.name), 'purchases': compras}

    @staticmethod
    def update_user(original_id: str, new_id: str, new_name: str):
        user = DBUser.query.filter_by(id=original_id).first()
        if not user:
            raise Exception(f"Usuario con ID '{original_id}' no existe")

        user.id = new_id
        user.name = new_name
        db.session.commit()

    @staticmethod
    def update_purchase(compra_id: int, new_data: dict):
        if not new_data:
            raise ValueError("No hay datos para actualizar")

        compra = DBTax.query.get(compra_id)
        if not compra:
            raise Exception("La compra no existe")

        for key, value in new_data.items():
            setattr(compra, key, value)

        db.session.commit()
        return True

    @staticmethod
    def delete_tax(user_id: str):
        DBTax.query.filter_by(user_id=user_id).delete()
        db.session.commit()

    @staticmethod
    def select_tax(user_id: str):
        compra = DBTax.query.filter_by(user_id=user_id).first()
        if compra:
            return TaxRecord(
                user_id=user_id,
                purchase=compra.purchase,
                porcentage=compra.porcentage,
                discount=compra.discount,
                plastic_bags=compra.plastic_bags,
                currency=compra.currency,
                tax_value=compra.tax_value
            )
        return None

    @staticmethod
    def delete_user(user_id: str):
        DBUser.query.filter_by(id=user_id).delete()
        db.session.commit()

    @staticmethod
    def delete_purchase(purchase_id: int):
        DBTax.query.filter_by(id=purchase_id).delete()
        db.session.commit()


