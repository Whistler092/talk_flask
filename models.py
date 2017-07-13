from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean, Date, func

db = SQLAlchemy()


class Lic(db.Model):
    __tablename__ = 'lics'

    id = Column(Integer, primary_key=True)
    serial = Column(String(64), index=True)
    name = Column(String(64), nullable=False)
    status = Column(Boolean)
    support_date = Column(Date, default=func.now())
