from structure import *
from config import db
import json


def insert_information_user(input_data):
    for item in input_data:
        db.session.add(
            User(
                id=item.get('id'),
                first_name=item.get('first_name'),
                last_name=item.get('last_name'),
                age=item.get('age'),
                email=item.get('email'),
                role=item.get('role'),
                phone=item.get('phone')
            )
        )
    db.session.commit()


def insert_information_order(input_data):
    for item in input_data:
        db.session.add(
            Order(
                id=item.get('id'),
                name=item.get('name'),
                description=item.get('description'),
                start_date=item.get('start_date'),
                end_date=item.get('end_date'),
                address=item.get('address'),
                price=item.get('price'),
                customer_id=item.get('customer_id'),
                executor_id=item.get('executor_id')
            )
        )
    db.session.commit()


def insert_information_offer(input_data):
    for item in input_data:
        db.session.add(
            Offer(
                id=item.get('id'),
                order_id=item.get('order_id'),
                executor_id=item.get('executor_id')
            )
        )
    db.session.commit()




def all_db():
    db.drop_all()
    db.create_all()

    with open('data/users.json', encoding='utf-8') as file:
        insert_information_user(json.load(file))

    with open('data/offers.json', encoding='utf-8') as file:
        insert_information_offer(json.load(file))

    with open('data/orders.json', encoding='utf-8') as file:
        insert_information_order(json.load(file))
