import sys
import os
import psycopg2

# Agregar la carpeta 'src' al path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from SecretConfig import DATABASE_URL

try:
    connection = psycopg2.connect(DATABASE_URL)
    print("✅ Conexión exitosa a la base de datos 💚")
    connection.close()
except Exception as e:
    print("❌ Error al conectar a la base de datos:")
    print(e)
