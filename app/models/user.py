from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, Boolean, Date, func
from app import db


class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    api_key = Column(String(64), unique=True, index=True)
