from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, String, DATETIME
from app.models import User

class Review(db.Model):
    __tablename__="reviews"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('products.id')), nullable=False)
    review = db.Column(db.String(255), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.String(), nullable=False)
    # updated_at = db.Column(db.String(), nullable=False)
    user = db.relationship("User", back_populates='reviews')

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'review': self.review,
            'rating': self.rating,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
