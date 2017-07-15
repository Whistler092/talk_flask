from flask_sqlalchemy import SQLAlchemy
from flask import url_for
from sqlalchemy import Column, Integer, String, Boolean, Date, func
from flask_login import UserMixin

db = SQLAlchemy()


class Lic(db.Model):
    __tablename__ = 'lics'

    id = Column(Integer, primary_key=True)
    serial = Column(String(64), index=True, nullable=False)
    name = Column(String(64), nullable=False)
    status = Column(Boolean, unique=False, default=True)
    support_date = Column(Date, default=func.now())

    @property
    def url(self):
        return url_for("get_lic", serial=self.serial)


class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    api_key = Column(String(64), unique=True, index=True)
