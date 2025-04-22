import datetime

import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Products(SqlAlchemyBase):
    __tablename__ = 'products'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    description = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    type = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("types.id"))
    sale = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    special_offer = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    cost = sqlalchemy.Column(sqlalchemy.Integer)
    img = sqlalchemy.Column(sqlalchemy.String, default='none.jpg')
    type_relation = orm.relationship('Types')

    def __repr__(self):
        return f'<products> {self.id} {self.title}'

    def add_during(self, data):
        self.during = data
