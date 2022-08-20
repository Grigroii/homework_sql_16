from structure import *


def get_all_users():
    '''Получение всех пользователей из таблицы User'''
    result = []
    for item in User.query.all():
        result.append(item.to_dict())
    return result


def get_user_by_id(user_id):
    '''Получение пользователя по id из таблицы User'''
    try:
        return db.session.query(User).filter(User.id == user_id).all()[0].to_dict()
    except Exception:
        return f'Not so user like {user_id}'


def get_all_orders():
    '''Получение всех информации из таблицы Order'''
    result = []
    for item in Order.query.all():
        result.append(item.to_dict())
    return result


def get_order_by_id(order_id):
    '''Получение информации о заказе по id из таблицы Order'''
    try:
        return db.session.query(Order).filter(Order.id == order_id)[0].to_dict()
    except Exception:
        return f'Not so order like {order_id}'


def get_all_offers():
    '''Получение всех информации из таблицы Offer'''
    result = []
    for item in Offer.query.all():
        result.append(item.to_dict())
    return result


def get_offer_by_id(offer_id):
    '''Получение информации о заказе  по id из таблицы Offer'''
    try:
        return db.session.query(Offer).filter(Offer.id == offer_id)[0].to_dict()
    except Exception:
        return f'Not so order like {offer_id}'


def get_update_data(model, user_id, values):
    '''Обновление данных в базе данных'''
    try:
        db.session.query(model).filter(model.id == user_id).update(values)

        db.session.commit()
    except Exception:
        return 'Error, not correct data'


def get_delete_data(model, user_id):
    '''Удаление данных в базе данных'''
    try:
        db.session.query(model).filter(model.id == user_id).delete()

        db.session.commit()
    except Exception:
        return 'Error, not correct data'
