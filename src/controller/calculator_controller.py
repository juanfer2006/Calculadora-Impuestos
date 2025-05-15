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

    def insert_tax(tax: TaxRecord):
        cursor = CalculatorController.GetCursor()
        consultation = f"""
            INSERT INTO taxes
            (user_id, purchase, porcentage, discount, plastic_bags, currency, tax_value)
            VALUES (
                '{tax.user_id}',
                {tax.purchase},
                {tax.porcentage},
                {tax.discount},
                {tax.plastic_bags},
                '{tax.currency}',
                {tax.tax_value}
            );
        """
        cursor.execute(consultation)
        cursor.connection.commit()

    def search(id: str):
        cursor = CalculatorController.GetCursor()
        consultation = f"""
                    select id_user, name_user
                    from users
                    where id_user = '{id}'
                    """
        cursor.execute(consultation)
        fila = cursor.fetchone()
        result = User(id=fila[0], name=fila[1])
        return result
    
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
