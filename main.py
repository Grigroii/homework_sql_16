from config import app
from functions import get_all_users, get_user_by_id, get_all_orders, get_all_offers, get_order_by_id, get_offer_by_id, \
    get_update_data, get_delete_data
from structure import User, Order, Offer
from utils import all_db, insert_information_user, insert_information_order, insert_information_offer
import json
from flask import request


@app.route("/users", methods=['GET', 'POST'])
def _get_all_users():
    result = get_all_users()
    if request.method == 'GET':
        return app.response_class(
            response=json.dumps(result, indent=4),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'POST':
        if isinstance(request.json, list):
            insert_information_user(request.json)
        if isinstance(request.json, dict):
            insert_information_user([request.json])
        else:
            print('Error in type of file')
        return app.response_class(
            response=json.dumps(request.json, indent=4),
            status=200,
            mimetype="application/json")


@app.route("/users/<int:user_id>", methods=['GET', 'PUT', 'DELETE'])
def get_user_by_pk(user_id):
    if request.method == 'GET':
        result = get_user_by_id(user_id)
        return app.response_class(
            response=json.dumps(result, indent=4),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'PUT':
        get_update_data(User, user_id, request.json)
        return app.response_class(
            response=json.dumps(['All correct'], ensure_ascii=False, indent=4),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'DELETE':
        get_delete_data(User, user_id)
        return app.response_class(
            response=json.dumps(['All delete'], ensure_ascii=False, indent=4),
            status=200,
            mimetype="application/json"
        )


@app.route("/orders", methods=['GET', 'POST'])
def get_orders():
    result = get_all_orders()
    if request.method == 'GET':
        return app.response_class(
            response=json.dumps(result, ensure_ascii=False, indent=4),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'POST':
        if isinstance(request.json, list):
            insert_information_order(request.json)
        if isinstance(request.json, dict):
            insert_information_order([request.json])
        else:
            print('Error in type of file')
        return app.response_class(
            response=json.dumps(request.json, indent=4),
            status=200,
            mimetype="application/json")


@app.route("/orders/<int:order_id>", methods=['GET', 'PUT', 'DELETE'])
def get_orders_by_pk(order_id):
    if request.method == 'GET':
        result = get_order_by_id(order_id)
        return app.response_class(
            response=json.dumps(result, ensure_ascii=False, indent=4),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'PUT':
        get_update_data(Order, order_id, request.json)
        return app.response_class(
            response=json.dumps(['All correct'], ensure_ascii=False, indent=4),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'DELETE':
        get_delete_data(Order, order_id)
        return app.response_class(
            response=json.dumps(['All delete'], ensure_ascii=False, indent=4),
            status=200,
            mimetype="application/json"
        )


@app.route("/offers", methods=['GET', 'POST'])
def get_offers():
    result = get_all_offers()
    if request.method == 'GET':
        return app.response_class(
            response=json.dumps(result, ensure_ascii=False, indent=4),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'POST':
        if isinstance(request.json, list):
            insert_information_offer(request.json)
        if isinstance(request.json, dict):
            insert_information_offer([request.json])
        else:
            print('Error in type of file')
        return app.response_class(
            response=json.dumps(request.json, indent=4),
            status=200,
            mimetype="application/json")


@app.route("/offers/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def get_offer_by_pk(id):
    if request.method == 'GET':
        result = get_offer_by_id(id)
        return app.response_class(
            response=json.dumps(result, indent=4),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'PUT':
        get_update_data(Offer, id, request.json)
        return app.response_class(
            response=json.dumps(['All correct'], ensure_ascii=False, indent=4),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'DELETE':
        get_delete_data(Offer, id)
        return app.response_class(
            response=json.dumps(['All delete'], ensure_ascii=False, indent=4),
            status=200,
            mimetype="application/json"
        )


if __name__ == '__main__':
    all_db()
    app.run(debug=True)
