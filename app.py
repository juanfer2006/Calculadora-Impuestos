from flask import Flask
import sys

sys.path.append("src")  

from model import db  # de model/__init__.py debe exportar 'db'
from model.db_models import User, TaxRecord  # tus modelos
from view.web import usuario  # tu blueprint

def create_app():
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        'postgresql://neondb_owner:npg_9Z0DOxvSpFto@ep-empty-fire-a886r058-pooler.eastus2.azure.neon.tech/neondb?sslmode=require'
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    
    with app.app_context():
        db.create_all()  # Crea todas las tablas definidas en los modelos
    
    app.register_blueprint(usuario.plano)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
