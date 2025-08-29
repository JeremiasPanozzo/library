from flask import Blueprint, jsonify, request
from .models import Author, Book
from .models import db
from flask_jwt_extended import jwt_required

bp = Blueprint('main', __name__)

@bp.route("/", methods=["GET"])
def index():
    welcome = "Welcome to this API!"
    return jsonify({"message": "Hello, World!", "welcome": welcome})

@bp.route('/authors', methods=['GET'])
def get_authors():
    try:
        authors = Author.query.all()
        authors_data = []
        for author in authors:
            author_data = {
                'name': author.name,
                'last_name': author.last_name,
                'id': author.id,
                'age': author.age,
                'books': []
            }
            for book in author.books:
                book_data = {
                    'id': book.id,
                    'isbn': book.isbn,
                    'name': book.name,
                    'page_count': book.page_count,
                    'created_at': book.created_at.isoformat() if book.created_at else None
                }
                author_data['books'].append(book_data)
            authors_data.append(author_data)
        return jsonify({'authors': authors_data})
    except Exception as error:
        print('Error', error)
        return jsonify({'message': 'Internal server error'}), 500
    
@bp.route('/authors', methods=['POST'])
@jwt_required()
def add_author():
    try:
        data = request.json
        
        if data is None:
            return jsonify({'message': 'Bad request, no data provided'}), 400
        
        name = data.get('name')
        last_name = data.get('last_name')
        age = data.get('age')

        if not name or not age or not last_name:
            return jsonify({'message': 'Bad request, name or age not found'}), 400
        
        try:
            age = int(age)
        except ValueError:
            return jsonify({'message': 'Invalid age format'}), 400

        new_author = Author(name=name, last_name=last_name, age=age)
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
                'page_count': book.page_count,
                'created_at': book.created_at.isoformat() if book.created_at else None
            }
            books_data.append(book_data)
        return jsonify({'books': books_data})
    except Exception as error:
        print('Error', error)
        return jsonify({'message': 'Internal server error'}), 500

@bp.route('/books', methods=['POST'])
@jwt_required()
def add_book():
    try:
        data = request.json

        if data is None:
            return jsonify({'message': 'Bad request, no data provided'}), 400
        
        isbn = data.get('isbn')
        name = data.get('name')
        page_count = data.get('page_count')
        author_id = data.get('author_id')

        if not name or not page_count or not author_id or not isbn:
            return jsonify({'message': 'Bad request, isbn or name or page_count or author not found'}), 400

        new_book = Book(isbn=isbn, name=name, page_count=page_count, author_id=author_id)
        db.session.add(new_book)
        db.session.commit()
        return jsonify({'book': {'id': new_book.id, 'isbn': new_book.isbn, 'name': new_book.name, 'page_count': new_book.page_count}}), 201
    except Exception as error:
        print('Error', error)
        return jsonify({'message': 'Internal server error'}), 500
    
@bp.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    try:
        book = Book.query.filter_by(id=book_id).first()

        if book is None:
            return jsonify({'message': 'Book not found'}), 404

        book_data = {
            'id': book.id,
            'isbn': book.isbn,
            'name': book.name,
            'page_count': book.page_count,
            'created_at': book.created_at.isoformat() if book.created_at else None
        }
        return jsonify({'book': book_data})
    except Exception as error:
        return jsonify({'message': 'Internal server error'}), 500
    
@bp.route('/books/<int:book_id>', methods=['DELETE'])
@jwt_required()
def delete_book(book_id):
    try:
        book = Book.query.filter_by(id=book_id).first()
        if book is None:
            return jsonify({'message': 'Book not found'}), 404

        db.session.delete(book)
        db.session.commit()
        return jsonify({'message': 'Book deleted successfully'}), 204
    except Exception as error:
        return jsonify({'message': 'Internal server error'}), 500
    
@bp.route('/authors/<int:author_id>', methods=['GET'])
def get_author(author_id):
    try:
        author = Author.query.filter_by(id=author_id).first()

        if author is None:
            return jsonify({'message':'Author not found'}), 404
        
        author_data = {
            'id': author.id,
            'name':author.name,
            'last_name': author.last_name,
            'age': author.age,
            'is_dead': author.is_dead,
            'created_at': author.created_at.isoformat() if author.created_at else None
        }

        return jsonify({'author': author_data})
    except Exception as error:
        return jsonify({'message': 'Internal server error'}), 500
    
@bp.route('/authors/<int:author_id>', methods=['DELETE'])
@jwt_required()
def delete_author(author_id):
    try:
        author = Author.query.filter_by(id=author_id).first()

        if author is None:
            return jsonify({'message': 'Author not found'}), 404
        
        db.session.delete(author)
        db.session.commit()

        return jsonify({'message': 'Author deleted successfully'}), 204
    except Exception as error:
        return jsonify({'message': 'Internal server error'}), 500