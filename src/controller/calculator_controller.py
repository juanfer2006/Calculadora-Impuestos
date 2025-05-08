import sys
sys.path.append('src')
sys.path.append( "." )
from model.calculator import Taxes, User
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