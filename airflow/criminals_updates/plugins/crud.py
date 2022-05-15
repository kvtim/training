from typing import List

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from criminal import Criminal, Base


class CRUD:
    def __init__(self):
        self.__engine = create_engine(f'sqlite:///criminals.sqlite')
        self.__Session = sessionmaker()
        self.__Session.configure(bind=self.__engine)
        self.__session = self.__Session()

    def create_criminals(self, criminals: List[Criminal]):
        Base.metadata.create_all(self.__engine)
        self.__session.add_all(criminals)
        self.__session.commit()

    def insert_criminal(self, criminal: Criminal):
        self.__session.add(criminal)
        self.__session.commit()

    def update_criminal(self, criminal: Criminal):
        self.__session.query(Criminal).filter_by(id=criminal.id).update({
            'fullname': criminal.fullname,
            'description': criminal.description,
            'url': criminal.url
        })
        self.__session.commit()

    def delete_criminal(self, criminal: Criminal):
        self.__session.query(Criminal).filter_by(id=criminal.id).delete()
        self.__session.commit()

    def select_criminals(self) -> List[Criminal]:
        return self.__session.query(Criminal).all()

