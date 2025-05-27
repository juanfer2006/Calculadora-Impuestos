from flask import Flask    
import sys
sys.path.append("src")

from model import db
from view.web import usuario

def create_app():
    app = Flask(__name__)
    
    # Configura tu base de datos aquí (ajusta la URI a la que uses)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'  
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)  # Vincula la instancia db con la app
    
    app.register_blueprint(usuario.plano)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
