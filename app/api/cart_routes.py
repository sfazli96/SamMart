from flask import Blueprint, jsonify, request
from app.models import db, cartJoined, User, Cart, Product
from sqlalchemy.orm import joinedload, session
from flask_login import login_required, current_user

cart_routes = Blueprint('cart', __name__)

@cart_routes.route('/<int:id>')
# @login_required
def readCart(id):
    carts = db.session.query(Cart).filter(Cart.user_id == id).all()
    # print('carts', carts)
    cart_result = []
    for cart in carts:
        all_product = []
        for product in cart.products:
            # print('product', product.to_dict())
            productObj = product.to_dict()
        all_product.append(productObj)

    cart_object = cart.to_dict()
    # print('cart_obj', cart_object)
    cart_object.update({"products": all_product})
    cart_result.append(cart_object)

    result = {
        "products": cart_result
    }
    # print('result',result)
    return result


@cart_routes.route('/', methods=['POST'])
def createCart():
    user = current_user
    print('user', user)
    request_data = request.get_json()
    new_cart = Cart(
        user_id = user.id
    )
    db.session.add(new_cart)
    db.session.commit()

    return new_cart.to_dict()


@cart_routes.route('/', methods=["PUT"])
def editCart():
    jsonData = request.get_json()
    product = Product.query.get(jsonData["product_id"])
    # print('PRODUCT!!!!!!!!', product)

    carts = db.session.query(Cart).filter(Cart.user_id == jsonData["user_id"]).options(joinedload(Cart.products))
    print('CARTS!!!!', carts)

    final_result = []
    for cart in carts:
        # print('cart loop', cart)
        cart_object = cart.to_dict()
        # print('cart_object', cart_object)
        cart.products.append(product)
        # result = [cart.to_dict() for cart in carts if cart.products.append(product)]
        db.session.commit()
        final_result.append(cart.to_dict())

    return final_result




@cart_routes.route('<int:id>', methods=['DELETE'])
def deleteCartItem(id):
    request_data = request.get_json()
    cart = Cart.query.get(id)
    print('cart', cart)
    if not cart:
        return cart.errors

    cart.products = [product for product in cart.products if product.id != request_data]
    print('list-----cart', cart.products)

    # for product in cart.products:
    #     if product.id == request_data:
    #         cart.product.remove(product)

    db.session.commit()

    cart_obj = {
        'id': cart.id,
        'product': [product.to_dict() for product in cart.products],
        'user_id': cart.user_id
    }
    # cart_obj = cart.to_dict()
    # cart_obj['products'] = []
    # for product in cart.products:
    #     if product.id == request_data:
    #         continue
    #     product_obj = product.to_dict()
    #     print('prod_obj', product_obj)
    #     cart_obj['products'].append(product_obj)

    return cart_obj

@cart_routes.route('<int:cart_id>/product/<int:product_id>', methods=['POST'])
def addItemToCart(cart_id, product_id):
    cart = Cart.query.get(cart_id)
    print('cart', cart)
    product = Product.query.get(product_id)
    print('product', product)

    cart.products.append(product)
    db.session.commit()

    return{"success": "Product added to cart"}



@cart_routes.route('/delete_cart', methods=['PUT'])
def emptyCart():
    cart_id = request.get_json()
    user_id = current_user.id
    print('user_id', user_id)
    carts = Cart.query.filter(Cart.id == cart_id).all()
    for cart in carts:
        cart.products.clear()
        db.session.commit()

    return {"Cart Emptied": user_id}