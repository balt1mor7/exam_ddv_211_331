import os
import sqlalchemy as sa
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from flask import url_for, current_app
from app import db


class Performance(db.Model):

    __tablename__ = 'performances'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return '<Performance %r>' % self.name


class User(db.Model, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(20), nullable=False)
    tel_number = db.Column(db.String(20), nullable=False)
    sms_code = db.Column(db.String(4), nullable=False)

    def __repr__(self) -> str:
        return '<User %r>' % self.login

class Ticket(db.Model):

    __tablename__ = 'tickets'

    id = db.Column(db.Integer, primary_key=True)
    performance_id = db.Column(db.Integer, db.ForeignKey(
        "performances.id"), nullable=False)
    sector = db.Column(db.String(1), nullable=False)
    place = db.Column(db.String(25), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(
        "users.id"), nullable=False)
    time = db.Column(db.Time, nullable=False)
    user = db.relationship('User')
    performance = db.relationship('Performance')


    def __repr__(self) -> str:
        return '<Ticket %r>' % self.place
