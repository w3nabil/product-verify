from . import db

# SQLAlchemy model class
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.String(20), unique=True)
    key = db.Column(db.String(120))
    name = db.Column(db.String(120))
    price = db.Column(db.String(120))
    manufacturer = db.Column(db.String(120))
    manufacture_date = db.Column(db.String(120))
    expiry_date = db.Column(db.String(120), default='LIFETIME')
    batch_number = db.Column(db.String(120))
