import sys
sys.path.append('src')
sys.path.append( "." )
from model.calculator import Taxes, User, TaxRecord
import psycopg2
import SecretConfig


class CalculatorController:
    def GetCursor():
        connection = psycopg2.connect(
            database=SecretConfig.PGDATABASE, 
            user=SecretConfig.PGUSER, 
            password=SecretConfig.PGPASSWORD, 
            host=SecretConfig.PGHOST, 
            port=SecretConfig.PGPORT
        )
        cursor = connection.cursor()
        return cursor

    def create_table():
        cursor = CalculatorController.GetCursor()
        with open('sql/create_table.sql', 'r') as archive:
            consultation = archive.read()
        cursor.execute(consultation)
        cursor.connection.commit() 

    def delete_table():
        cursor = CalculatorController.GetCursor()
        with open('sql/delete_table.sql', 'r') as archive:
            consultation = archive.read()
        cursor.execute(consultation)
        cursor.connection.commit()
    
    def insert(user: User):
        cursor = CalculatorController.GetCursor()
        consultation = f"""
                    insert into users
                    (id_user, name_user)
                    values ('{user.id}', '{user.name}');
                    """
        cursor.execute(consultation)
        cursor.connection.commit()

    @staticmethod
    def insert_tax(tax: TaxRecord):
        cursor = CalculatorController.GetCursor()
        
        # Validar y calcular el impuesto ANTES de insertar
        try:
            tax_value = Taxes.calculate(
                purchase=tax.purchase,
                porcentage=tax.porcentage,
                discount=tax.discount,
                plastic_bag=tax.plastic_bags,
                currency=tax.currency
            )
            
            # Actualizar el valor del impuesto en el objeto
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
            raise e  # Re-lanzamos la excepción para manejarla en la ruta Flask

    def search(id: str):
        cursor = CalculatorController.GetCursor()

        # Obtener datos del usuario
        consulta_usuario = f"""
            SELECT id_user, name_user
            FROM users
            WHERE id_user = '{id}'
        """
        cursor.execute(consulta_usuario)
        fila_usuario = cursor.fetchone()

        if not fila_usuario:
            return None

        user = User(id=fila_usuario[0], name=fila_usuario[1])

        # Obtener compras del usuario
        consulta_compras = f"""
            SELECT purchase, porcentage, discount, plastic_bags, currency, tax_value
            FROM taxes
            WHERE user_id = '{id}'
        """
        cursor.execute(consulta_compras)
        filas_compras = cursor.fetchall()

        compras = [
            {
                'purchase': row[0],
                'porcentage': row[1],
                'discount': row[2],
                'plastic_bags': row[3],
                'currency': row[4],
                'tax_value': row[5]
            }
            for row in filas_compras
        ]

        return {'user': user, 'purchases': compras}


    
    def update_tax(tax: TaxRecord):
        cursor = CalculatorController.GetCursor()
        consultation = f"""
            UPDATE taxes
            SET 
                purchase = {tax.purchase},
                porcentage = {tax.porcentage},
                discount = {tax.discount},
                plastic_bags = {tax.plastic_bags},
                currency = '{tax.currency}',
                tax_value = {tax.tax_value}
            WHERE user_id = '{tax.user_id}';
        """
        cursor.execute(consultation)
        cursor.connection.commit()

    def delete_tax(user_id: str):
        cursor = CalculatorController.GetCursor()
        consultation = f"""
            DELETE FROM taxes WHERE user_id = '{user_id}';
        """
        cursor.execute(consultation)
        cursor.connection.commit()

    def select_tax(user_id: str):
        cursor = CalculatorController.GetCursor()
        consultation = f"""
            SELECT purchase, porcentage, discount, plastic_bags, currency, tax_value
            FROM taxes
            WHERE user_id = '{user_id}';
        """
        cursor.execute(consultation)
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
        consultation = f"DELETE FROM users WHERE id_user = '{user_id}'"
        cursor.execute(consultation)
        cursor.connection.commit()

    @staticmethod
    def delete_purchase(purchase_id: int):
        cursor = CalculatorController.GetCursor()
        consultation = f"DELETE FROM taxes WHERE id = {purchase_id}"
        cursor.execute(consultation, (purchase_id,))
        cursor.connection.commit() 

    @staticmethod
    def update_purchase(compra_id: int, new_data: dict):
        cursor = CalculatorController.GetCursor()
        
        try:
            # Construir la consulta SQL dinámicamente
            set_clause = ", ".join([f"{key} = %s" for key in new_data.keys()])
            values = list(new_data.values())
            values.append(compra_id)  # Para el WHERE
            
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

