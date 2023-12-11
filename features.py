import json
from json import JSONDecodeError
import random
from datetime import datetime


def get_all_books():
    try:
        with open("books.json") as f:
            all_books: list = json.load(f)
            f.close()
        return all_books
    except (FileNotFoundError, JSONDecodeError):
        with open("books.json", "w") as f:
            json.dump([], f, indent=4)
            f.close()
        with open("books.json") as f:
            all_books: list = json.load(f)
            f.close()
        return all_books


class Book:
    def __init__(self, title, author, genre, language, price):
        self.title = title
        self.author = author
        self.genre = genre
        self.language = language
        self.price = price

    def add_to_database(self):
        rand_n = random.randint(1, 100)
        book = {
            'id': rand_n,
            'title': self.title,
            'author': self.author,
            'genre': self.genre,
            'language': self.language,
            'price': self.price
        }
        if self.isavailable():
            all_data = get_all_books()
            all_data.append(book)
            with open("books.json", "w") as f:
                json.dump(all_data, f, indent=4)
                f.close()
            return rand_n
        else:
            print("add diferent book your book is available in library")

    def isavailable(self):
        all_data = get_all_books()
        k = 0
        for b in all_data:
            if self.title == b['title'] and self.author == b['author']:
                return False
            else:
                k += 1
        if k == len(all_data):
            return True


def add_books():
    title = input("enter title: ")
    author = input("enter author: ")
    genre = input("enter genre: ")
    language = input("enter language: ")
    price = input("enter price")
    price = price + "$"
    book_obj = Book(title, author, genre, language, price)
    book_id = book_obj.add_to_database()
    return book_id


def delete_book():
    all_books = get_all_books()
    book_id = int(input("enter your book's id to delete: "))
    k = 0
    for b in all_books:
        if b['id'] == book_id:
            all_books.remove(b)
            print("your book was deleted")
            with open("books.json", "w") as f:
                json.dump(all_books, f, indent=4)
                f.close()
        else:
            k += 1
    if k == len(all_books):
        print("your book id is not valid")

def edit_book():
    all_books = get_all_books()
    book_id = int(input("enter your book's id to edit: "))
    k = 0
    for b in all_books:
        if b['id'] == book_id:
            title = input("enter title: ")
            author = input("enter author: ")
            genre = input("enter genre: ")
            language = input("enter language: ")
            price = input("enter price")
            price = price + "$"
            b['title'] = title
            b['author'] = author
            b['genre'] = genre
            b['language'] = language
            b['price'] = price
            print("your book was edited")
            with open("books.json", "w") as f:
                json.dump(all_books, f, indent=4)
                f.close()
        else:
            k += 1
    if k == len(all_books):
        print("your book's id is not found")

def show_all_books():
    all_books = get_all_books()
    for i in all_books:
        print(i)

def search_with_title(userid):
    all_books = get_all_books()
    title = input("enter title to search book")
    k = 0
    for b in all_books:
        if b['title'] == title:
            print(b)
            check_b = int(input("1 to buy the book"))
            if check_b == 1:
                buy_book(b['id'], userid)
        else:
            k += 1
    if k == len(all_books):
        print(f"book was not found with this {title} title")

def search_with_author(userid):
    all_books = get_all_books()
    author = input("enter title to search book")
    k = 0
    for b in all_books:
        if b['author'] == author:
            print(b)
            check_b = int(input("1 to buy the book"))
            if check_b == 1:
                buy_book(b['id'], userid)
        else:
            k += 1
    if k == len(all_books):
        print(f"book was not found with this {author} title")

def buy_book(book_id, userid):
    all_books = get_all_books()
    for b in all_books:
        if b['id'] == book_id:
            s = {
                'sold_at': str(datetime.now()),
                'sold_book': b['id'],
                'bought_userid': userid
            }
            all_sold_books = get_all_sold_books()
            all_sold_books.append(s)
            with open("soldbooks.json", "w") as f:
                json.dump(all_sold_books, f, indent=4)
                f.close()
            print("you bought the book successfully")


def get_all_sold_books():
    try:
        with open("soldbooks.json") as f:
            all_sold_books: list = json.load(f)
            f.close()
        return all_sold_books
    except (FileNotFoundError, JSONDecodeError):
        with open("soldbooks.json", "w") as f:
            json.dump([], f, indent=4)
            f.close()
        with open("soldbooks.json") as f:
            all_sold_books: list = json.load(f)
            f.close()
        return all_sold_books
