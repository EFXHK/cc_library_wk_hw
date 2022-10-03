# from models.book import Book
from models.book import *


#list of available books
book1 = Book("The Structural Dynamics of Flow", "L.G Claret", "Engineering")#, False)
book2 = Book("History of Straws", "Strawman", "History")#, True)



books = [book1, book2]      #shouldve used more informative variable name

def save_book(new_book):
    books.append(new_book)

def single_book(single_book):
    single_book = books[int(0)]  #<<<<<<<
    return single_book

# def remove_book(title):
#     for book in books:
#         if book.title == title:
#             books.remove(book)
