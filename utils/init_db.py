from .db_connection import Database


def init_db():
    """Initialize all database tables"""
    db = Database()  # create database instance
    db.init_db()
