from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

books = [
    {"id": 1, "title": "Book 1", "author": "Author 1"},
    {"id": 2, "title": "Book 2", "author": "Author 2"},
    {"id": 3, "title": "Book 3", "author": "Author 3"}
]

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/books", methods=["GET"])
def get_all_books():
    return jsonify({"books": books})

@app.route("/books/<int:book_id>", methods=["GET"])
def get_book_by_id(book_id):
    book = next((b for b in books if b["id"] == book_id), None)
    if book:
        return jsonify({"book": book})
    else:
        return jsonify({"error": "Book not found"}), 404

@app.route("/books", methods=["POST"])
def add_book():
    new_book = request.json
    new_book["id"] = max(b["id"] for b in books) + 1
    books.append(new_book)
    return jsonify({"message": "Book added successfully", "book": new_book}), 201

@app.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    book_to_update = next((b for b in books if b["id"] == book_id), None)
    if book_to_update:
        updated_book_data = request.json
        book_to_update.update(updated_book_data)
        return jsonify({"message": "Book updated successfully", "book": book_to_update})
    else:
        return jsonify({"error": "Book not found"}), 404

@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    global books
    books = [b for b in books if b["id"] != book_id]
    return jsonify({"message": "Book deleted successfully"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
