import sys
sys.path.append('src')
sys.path.append( "." )
from model.calculator import Taxes, User
import psycopg2
import SecretConfig


class CalculatorController:
    def ObtenerCursor():
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
        cursor = CalculatorController.ObtenerCursor()
        with open('sql/create_table.sql', 'r') as archive:
            consultation = archive.read()
        cursor.execute(consultation)
        cursor.connection.commit() 

    def delete_table():
        cursor = CalculatorController.ObtenerCursor()
        with open('sql/delete_table.sql', 'r') as archive:
            consultation = archive.read()
        cursor.execute(consultation)
        cursor.connection.commit()
    
    def insert(user: User):
        cursor = CalculatorController.ObtenerCursor()
        consulta = f"""
                    insert into users
                    (id_user, name_user)
                    values ('{user.id}', '{user.name}');
                    """
        cursor.execute(consulta)
        cursor.connection.commit()

    def search(id: str):
        cursor = CalculatorController.ObtenerCursor()
        consulta = f"""
                    select id_user, name_user
                    from users
                    where id_user = '{id}'
                    """
        cursor.execute(consulta)
        fila = cursor.fetchone()
        resultado = User(id=fila[0], name=fila[1])
        return resultado