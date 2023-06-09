from flask import Blueprint, jsonify, request
from app.models import Favorite, User, db
from flask_login import login_required, current_user
from datetime import datetime


favorite_routes = Blueprint('favorites', __name__)

@favorite_routes.route('/', methods = ['POST'])
def create_favorites():
    created_at = datetime.now()
    request_data = request.get_json()

    favorite = Favorite(
        user_id = request_data["user_id"],
        product_id = request_data["product_id"],
        created_at = created_at
    )
    # print('FAV-----------------------', favorite)
    db.session.add(favorite)
    db.session.commit()

    return favorite.to_dict()


@favorite_routes.route('/<int:user_id>', methods=['GET'])
def get_favorites(user_id):
    favorites = Favorite.query.filter_by(user_id = user_id).all()
    # print('FAV---------', favorites)
    fav_dict = [favorite.to_dict() for favorite in favorites]
    # print('DICT----------', fav_dict)
    return jsonify(fav_dict)


@favorite_routes.route('/<int:id>', methods=['DELETE'])
def delete_favorite(id):
    favorite = Favorite.query.filter_by(product_id = id).first()
    # favorite = Favorite.query.get(id)
    # print('FAVOR', favorite.to_dict())
    if favorite:
        db.session.delete(favorite)
        db.session.commit()
        return favorite.to_dict()
    else:
        return {"error": "Favorite not found"}, 404
