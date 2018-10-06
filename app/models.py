from werkzeug.security import generate_password_hash
from app import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    password = db.Column(db.String(255))
    age = db.Column(db.Integer)

    def __init__(self, username, userpassword, userage):
        self.name = username
        self.password = generate_password_hash(userpassword)
        self.age = userage

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return "<Users: {}>".format(self.name)
