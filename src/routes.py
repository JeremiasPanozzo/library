from flask import Blueprint, jsonify, request
from .models import Author, Book
from .models import db

bp = Blueprint('main', __name__)

@bp.route("/", methods=["GET"])
def index():
    user_agent = request.headers.get("User-Agent")
    return jsonify({"message": "Hello, World!", "user_agent": user_agent})

@bp.route('/authors', methods=['GET'])
def get_authors():
    try:
        authors = Author.query.all()
        authors_data = []
        for author in authors:
            author_data = {
                'id': author.id,
                'name': author.name,
                'age': author.age,
                'books': []
            }
            for book in author.books:
                book_data = {
                    'id': book.id,
                    'isbn': book.isbn,
                    'name': book.name,
                    'cant_pages': book.cant_pages,
                    'createdAt': book.created_at.isoformat() if book.created_at else None
                }
                author_data['books'].append(book_data)
            authors_data.append(author_data)
        return jsonify({'authors': authors_data})
    except Exception as error:
        print('Error', error)
        return jsonify({'message': 'Internal server error'}), 500
    
@bp.route('/authors', methods=['POST'])
def add_author():
    try:
        data = request.json
        name = data.get('name')
        age = data.get('age')
        if not name or not age:
            return jsonify({'message': 'Bad request, name or age not found'}), 400
        new_author = Author(name=name, age=age)
        db.session.add(new_author)
        db.session.commit()
        return jsonify({'author': {'id': new_author.id, 'name': new_author.name, 'age': new_author.age}}), 201
    except Exception as error:
        print('Error', error)
        return jsonify({'message': 'Internal server error'}), 500
    
@bp.route('/books', methods=['GET'])
def get_books():
    try:
        books = Book.query.all()
        books_data = []
        for book in books:
            book_data = {
                'id': book.id,
                'isbn': book.isbn,
                'name': book.name,
                'cant_pages': book.cant_pages,
                'createdAt': book.created_at.isoformat() if book.created_at else None
            }
            books_data.append(book_data)
        return jsonify({'books': books_data})
    except Exception as error:
        print('Error', error)
        return jsonify({'message': 'Internal server error'}), 500

@bp.route('/books', methods=['POST'])
def add_book():
    try:
        data = request.json
        isbn = data.get('isbn')
        name = data.get('name')
        cant_pages = data.get('cant_pages')
        author_id = data.get('author_id')
        if not name or not cant_pages or not author_id or not isbn:
            return jsonify({'message': 'Bad request, isbn or name or cantPages or author not found'}), 400
        new_book = Book(isbn=isbn, name=name, cant_pages=cant_pages, author_id=author_id)
        db.session.add(new_book)
        db.session.commit()
        return jsonify({'book': {'id': new_book.id, 'isbn': new_book.isbn, 'name': new_book.name, 'cant_pages': new_book.cant_pages}}), 201
    except Exception as error:
        print('Error', error)
        return jsonify({'message': 'Internal server error'}), 500