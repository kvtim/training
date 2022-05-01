from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Criminal(Base):
    __tablename__ = 'criminal'

    id = Column(String, primary_key=True)
    fullname = Column(String)
    description = Column(String)
    url = Column(String)

    def __init__(self, id, fullname, description, url):
        self.id = id
        self.fullname = fullname
        self.description = description
        self.url = url

    def __repr__(self):
        return f"Criminal(id={self.id}, fullname={self.fullname}, description={self.description}, url={self.url})"

