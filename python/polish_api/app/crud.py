from typing import List

from app import db


class CRUD:
    @staticmethod
    def select_all(item_class):
        return item_class.query.all()

    @staticmethod
    def select_by_id(item_class, item_id):
        return item_class.query.get(item_id)

    @staticmethod
    def insert(item):
        db.session.add(item)
        db.session.commit()

    @staticmethod
    def insert_list(items: List):
        db.session.add_all(items)
        db.session.commit()

    @staticmethod
    def delete(item):
        db.session.delete(item)
        db.session.commit()

    @staticmethod
    def update(item_class, item_id, **kwargs):
        item_class.query.filter_by(id=item_id).update(kwargs)
        db.session.commit()
