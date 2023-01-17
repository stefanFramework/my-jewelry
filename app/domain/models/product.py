from domain.models import BaseModel, db

class Product(BaseModel):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=True)
    image_path = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)