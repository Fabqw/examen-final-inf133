import json

from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from app.database import db


class User(UserMixin, db.Model):
    __tablename__ = "users"

    #id: Identificador único del usuario. De tipo entero y autoincremental.
    #name: Nombre del usuario. De tipo cadena de texto.
    #email: Correo electrónico del usuario. De tipo cadena de texto.
    #password: Contraseña del usuario. De tipo cadena de texto.
    #phone: Número de teléfono del usuario. De tipo cadena de texto.
    #role: Rol del usuario (admin, customer). De tipo cadena de texto.

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    phone = db.Column(db.String(50), primary_key=True)
    role = db.Column(db.String(50), nullable=False)

    def __init__(self, email, name,password, phone, role):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)
        self.phone = phone
        self.role = role

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def find_by_email(email):
        return User.query.filter_by(email=email).first()