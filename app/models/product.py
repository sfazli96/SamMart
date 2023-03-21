from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.orm import relationship
# from app.models.shopping_cart import cartJoined
# from app.models.order import orderJoined

class Product(db.Model):
    __tablename__="product"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    price = db.Column(db.Float(), nullable=False)
    image_url = db.Column(db.String(1000), nullable=False)
    size = db.Column(db.String(25), nullable=False)
    # cartJoined = db.relationship("Cart", back_populates="products", secondary=cartJoined)
    # orderJoined = db.relationship("Order", back_populates="products", secondary=orderJoined)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'image_url': self.image_url,
            'size': self.size
        }