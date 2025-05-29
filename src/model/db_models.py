from model import db

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)
    
    taxes = db.relationship('TaxRecord', backref='user', cascade="all, delete-orphan")

    def is_equal(self, other):
        assert self.id == other.id, 'El id no coincide'
        assert self.name == other.name, 'El nombre no coincide'
        return True

class TaxRecord(db.Model):
    __tablename__ = 'taxes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # agregar autoincrement por claridad
    user_id = db.Column(db.String, db.ForeignKey('users.id'), nullable=False)
    purchase = db.Column(db.Float, nullable=False)
    porcentage = db.Column(db.Integer, nullable=False)
    discount = db.Column(db.Float, nullable=False)
    plastic_bags = db.Column(db.Integer, nullable=False)
    currency = db.Column(db.String, nullable=False)
    tax_value = db.Column(db.Float, nullable=False)

    def is_equal(self, other):
        assert self.user_id == other.user_id, "El id de usuario no coincide"
        assert self.purchase == other.purchase, "El valor de compra no coincide"
        assert self.porcentage == other.porcentage, "El porcentaje no coincide"
        assert self.discount == other.discount, "El descuento no coincide"
        assert self.plastic_bags == other.plastic_bags, "La cantidad de bolsas no coincide"
        assert self.currency == other.currency, "La moneda no coincide"
        assert self.tax_value == other.tax_value, "El impuesto calculado no coincide"
        return True
