# test/test_db.py

import sys
import os
sys.path.append(os.path.abspath("src"))

from model import db
from model.db_models import User, TaxRecord
from flask import Flask

def create_test_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        'postgresql://neondb_owner:npg_9Z0DOxvSpFto@ep-empty-fire-a886r058-pooler.eastus2.azure.neon.tech/neondb?sslmode=require'
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    return app

app = create_test_app()

with app.app_context():
    print("Creando tablas si no existen...")
    db.create_all()

    print("Insertando usuario de prueba...")
    test_user = User(id="123", name="Kevin Test")
    db.session.add(test_user)

    print("Insertando impuesto de prueba...")
    test_tax = TaxRecord(
        user_id="123",
        purchase=100000,
        porcentage=19,
        discount=10,
        plastic_bags=2,
        currency='COP',
        tax_value=17135.0
    )
    db.session.add(test_tax)

    db.session.commit()
    print("Datos de prueba insertados correctamente.")

    # Verificación de datos
    user = User.query.get("123")
    tax = TaxRecord.query.filter_by(user_id="123").first()

    assert user is not None, "❌ Usuario no fue insertado correctamente."
    assert tax is not None, "❌ Impuesto no fue insertado correctamente."

    print("✅ Prueba completada con éxito: se insertaron los datos correctamente.")

