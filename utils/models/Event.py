from utils.db_connection import db


class Event(db.Model):
    __tablename__ = "events"

    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(80), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    date = db.Column(db.String(80), nullable=False)
    location = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(80), nullable=False)
    runtime = db.Column(db.String(80), nullable=False)
    price = db.Column(db.String(80), nullable=False)
