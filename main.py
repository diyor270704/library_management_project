from register_and_login import register, login, login_as_admin
from features import add_books, delete_book, edit_book, show_all_books, search_with_title, search_with_author, buy_book


print("welcome to library. here you can identify books to buy.\nif you are admin you can add and sell your books")

check_r = int(input("1 to register\n2 to login\n3 to login as admin"))
k = 0
r = False
if check_r == 1:
    r = register()
if check_r == 2 or r:
    k = login()
    if k != 0:
        print("you logged in")
        check_s = int(input("1 to see all books\n2 to search books with title\n3 to search books with author"))
        if check_s == 1:
            show_all_books()
            book_id = int(input("enter book's id to buy that book: "))
            buy_book(book_id, k)
        elif check_s == 2:
            search_with_title(k)
        elif check_s == 3:
            search_with_author(k)

    else:
        print("username or password incorrect")
if check_r == 3:
    userid = login_as_admin()
    if userid != 0:
        print("you logged as an admin successfully")
        check_b = int(input("1 to add book\n2 to delete your book\n3 to edit your book"))
        if check_b == 1:
            book_id = add_books()
            print(f"your book id is {book_id}.\nyou will need this to delete and edit your book")
        elif check_b == 2:
            delete_book()
        elif check_b == 3:
             edit_book()
    else:
        print("make sure you are admin")


