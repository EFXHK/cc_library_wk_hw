from flask import render_template, request, redirect
from app import app
from models.book_list import books, save_book#,remove_book
from models.book import Book


#pathing to homepage
@app.route("/")
def index():
    return render_template("index.html", title="CodeClan Library", book=books)


@app.route("/single_book")
def single_book():
    return render_template("single_book.html")

@app.route("/books", methods=["POST"])
def add_book():
    book_title = request.form["title"]
    book_author = request.form["author"]
    book_genre = request.form["genre"]
    new_book = Book(book_title, book_author, book_genre)
    save_book(new_book)
    return redirect("/")


# @app.route("/books/remove_book/<title>", methods=["post"])
# def remove_book(title):
#     remove_book(title)
#     return redirect("/")
# ##### comment in line 3 ########


