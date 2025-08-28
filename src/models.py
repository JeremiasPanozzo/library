from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = "authors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    is_dead = db.Column(db.Boolean, nullable=False, default=False)
    age = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    books = db.relationship("Book", backref="author", cascade="all, delete-orphan")

    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age

class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(255), nullable=False, unique=True)
    name = db.Column(db.String(255), nullable=False)
    page_count = db.Column(db.Integer, nullable=False, default=0)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)

    def __init__(self, isbn, name, page_count, author_id) -> None:
        self.isbn = isbn
        self.name = name
        self.page_count = page_count
        self.author_id = author_id