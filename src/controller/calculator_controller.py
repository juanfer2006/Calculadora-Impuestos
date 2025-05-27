import sys
sys.path.append('src')

from model.calculator import Taxes, User, TaxRecord
import psycopg2
import SecretConfig


class CalculatorController:

    @staticmethod
    def GetCursor():
        # Conexión directa usando DATABASE_URL para Neon
        connection = psycopg2.connect(SecretConfig.DATABASE_URL)
        cursor = connection.cursor()
        return cursor

    @staticmethod
    def create_table():
        cursor = CalculatorController.GetCursor()
        with open('sql/create_table.sql', 'r') as archive:
            consultation = archive.read()
        cursor.execute(consultation)
        cursor.connection.commit()

    @staticmethod
    def delete_table():
        cursor = CalculatorController.GetCursor()
        with open('sql/delete_table.sql', 'r') as archive:
            consultation = archive.read()
        cursor.execute(consultation)
        cursor.connection.commit()

    @staticmethod
    def insert(user: User):
        cursor = CalculatorController.GetCursor()
        consultation = """
            INSERT INTO users (id_user, name_user)
            VALUES (%s, %s)
        """
        cursor.execute(consultation, (user.id, user.name))
        cursor.connection.commit()

    @staticmethod
    def insert_tax(tax: TaxRecord):
        cursor = CalculatorController.GetCursor()
        try:
            tax_value = Taxes.calculate(
                purchase=tax.purchase,
                porcentage=tax.porcentage,
                discount=tax.discount,
                plastic_bag=tax.plastic_bags,
                currency=tax.currency
            )
            tax.tax_value = tax_value

            consultation = """
                INSERT INTO taxes
                (user_id, purchase, porcentage, discount, plastic_bags, currency, tax_value)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(consultation, (
                tax.user_id,
                tax.purchase,
                tax.porcentage,
                tax.discount,
                tax.plastic_bags,
                tax.currency,
                tax.tax_value
            ))
            cursor.connection.commit()
            return True
        except Exception as e:
            cursor.connection.rollback()
            raise e

    @staticmethod
    def search(id: str):
        cursor = CalculatorController.GetCursor()

        cursor.execute("""
            SELECT id_user, name_user
            FROM users
            WHERE id_user = %s
        """, (id,))
        fila_usuario = cursor.fetchone()

        if not fila_usuario:
            return None

        user = User(id=fila_usuario[0], name=fila_usuario[1])

        cursor.execute("""
            SELECT id, purchase, porcentage, discount, plastic_bags, currency, tax_value
            FROM taxes
            WHERE user_id = %s
        """, (id,))
        filas_compras = cursor.fetchall()

        compras = [
            {
                'id': row[0],
                'purchase': row[1],
                'porcentage': row[2],
                'discount': row[3],
                'plastic_bags': row[4],
                'currency': row[5],
                'tax_value': row[6]
            }
            for row in filas_compras
        ]

        return {'user': user, 'purchases': compras}

    @staticmethod
    def update_user(original_id: str, new_id: str, new_name: str):
        cursor = CalculatorController.GetCursor()
        try:
            cursor.execute("SELECT id_user FROM users WHERE id_user = %s", (original_id,))
            if cursor.rowcount == 0:
                raise Exception(f"Usuario con ID '{original_id}' no existe")

            cursor.execute("""
                UPDATE users
                SET id_user = %s, name_user = %s
                WHERE id_user = %s
            """, (new_id, new_name, original_id))

            cursor.connection.commit()
        except Exception as e:
            cursor.connection.rollback()
            raise e

    @staticmethod
    def update_purchase(compra_id: int, new_data: dict):
        cursor = CalculatorController.GetCursor()
        try:
            set_clause = ", ".join([f"{key} = %s" for key in new_data.keys()])
            values = list(new_data.values())
            values.append(compra_id)

            consultation = f"""
                UPDATE taxes
                SET {set_clause}
                WHERE id = %s
            """

            cursor.execute(consultation, values)
            cursor.connection.commit()
            return True

        except Exception as e:
            cursor.connection.rollback()
            raise e

    @staticmethod
    def delete_tax(user_id: str):
        cursor = CalculatorController.GetCursor()
        consultation = "DELETE FROM taxes WHERE user_id = %s"
        cursor.execute(consultation, (user_id,))
        cursor.connection.commit()

    @staticmethod
    def select_tax(user_id: str):
        cursor = CalculatorController.GetCursor()
        consultation = """
            SELECT purchase, porcentage, discount, plastic_bags, currency, tax_value
            FROM taxes
            WHERE user_id = %s
            LIMIT 1
        """
        cursor.execute(consultation, (user_id,))
        fila = cursor.fetchone()
        if fila:
            return TaxRecord(
                user_id=user_id,
                purchase=fila[0],
                porcentage=fila[1],
                discount=fila[2],
                plastic_bags=fila[3],
                currency=fila[4],
                tax_value=fila[5]
            )
        return None

    @staticmethod
    def delete_user(user_id: str):
        cursor = CalculatorController.GetCursor()
        consultation = "DELETE FROM users WHERE id_user = %s"
        cursor.execute(consultation, (user_id,))
        cursor.connection.commit()

    @staticmethod
    def delete_purchase(purchase_id: int):
        cursor = CalculatorController.GetCursor()
        consultation = "DELETE FROM taxes WHERE id = %s"
        cursor.execute(consultation, (purchase_id,))
        cursor.connection.commit()

