import sqlite3
import datetime
from Librarian import librarian
from Librarian import BOOKS
from Librarian import USERS

connection = sqlite3.connect('Library_Database.db')

cursor = connection.cursor()

query = '''CREATE TABLE IF NOT EXISTS librarians(
            First_Name text,
            Last_Name text,
            Contact_Info text)'''
cursor.execute(query)

query = '''CREATE TABLE IF NOT EXISTS books(
            Book_Name text,
            Author_Name text,
            ID int,
            Publication_Company text,
            Rent_Y_N text,
            Rent_date text,
            Rent_Username text)'''
cursor.execute(query)

query = '''CREATE TABLE IF NOT EXISTS user(
            User_First_Name text,
            User_Last_Name text,
            username text,
            password text,
            contact text,
            fee integer,
            book_rented text) '''
cursor.execute(query)


# Add librarian


def insert_librarian(lib):
    with connection:
        cursor.execute("INSERT INTO librarians VALUES(:First_Name,:Last_Name,:Contact_Info)", {'First_Name': lib.first, 'Last_Name': lib.last, 'Contact_Info': lib.contact})

# Search Librarian by last name


def get_librarian_by_name(lastname):
    with connection:
        cursor.execute("SELECT * FROM librarians WHERE Last_Name=:Last_Name", {'Last_Name': lastname})
        return cursor.fetchall()

# BOOKS


def insert_books(book):
    with connection:
        cursor.execute("INSERT INTO books VALUES(:Book_Name,:Author_Name,:ID, :Publication_Company,:Rent_Y_N,:Rent_date, :Rent_Username)", {'Book_Name': book.bookname, 'Author_Name': book.authorname, 'ID': book.Identity, 'Publication_Company': book.publicationcompany, 'Rent_Y_N': book.Rent, 'Rent_date': book.rentdate, 'Rent_Username': book.username})

# Returns books that are not rented


def get_available_books(available):
    with connection:
        cursor.execute("SELECT * FROM books WHERE Rent_Y_N= :Rent_Y_N", {'Rent_Y_N': available})
        return cursor.fetchall()

# Returns books that are rented


def get_rented_books(rented):
    with connection:
        cursor.execute("SELECT * FROM books WHERE Rent_Y_N= :Rent_Y_N", {'Rent_Y_N': rented})
        return cursor.fetchall()

# Update rental information of a book


def update_books(rent_YN, date, bookusername, ID):
    with connection:
        cursor.execute('UPDATE books SET Rent_Y_N=:Rent_Y_N, Rent_date=:Rent_date, Rent_Username=:Rent_Username WHERE ID=:ID', {'Rent_Y_N': rent_YN, 'Rent_date': date, 'Rent_Username': bookusername, 'ID': ID})

# Delete books from the database


def del_books(bookid, booksname):
    with connection:
        cursor.execute('DELETE FROM books WHERE ID=:ID AND Book_Name=:Book_Name', {'ID': bookid, 'Book_Name': booksname})

# USER


def insert_users(cust):
    with connection:
        cursor.execute("""INSERT INTO user VALUES(:User_First_Name, :User_Last_Name,:username, :password, :contact,:fee,:book_rented)""", {'User_First_Name': cust.first, 'User_Last_Name': cust.last, 'username': cust.USERname, 'password': cust.password, 'contact': cust.contactdetails, 'fee': cust.fee, 'book_rented': cust.bookrented})

# Returns already registered users/acts as a login instrument


def old_user(userID, user_password):
    with connection:
        cursor.execute("SELECT * FROM user WHERE username=:username AND password=:password", {'username': userID, 'password': user_password})
        return cursor.fetchall()


def update_user(newusername, newpassword, contact):
    with connection:
        cursor.execute("UPDATE user SET username=:username, password=:password WHERE contact=:contact", {'username': newusername, 'password': newpassword, 'contact': contact})

# delete users


def del_user(userID, user_password):
    with connection:
        cursor.execute('DELETE FROM user WHERE username=:username AND password=:password', {'username': userID, 'password': user_password})


interfaceloop = 'a'

while (interfaceloop == 'a'):

    interface = input('press a for a new librarian\npress b for existing\npress c for adding a new book\npress d to see books available for rent\npress f to see books rented\npress g to update book\n press h to update book\npress i to add new user or login\n press j to delete user\npress k to update username and password\n')

    if interface == 'a':

        Add_librarian = input('Add new Librarian: YES/NO:')

        if Add_librarian == 'YES':

            lib_1 = librarian('firstname', 'last', 'contact')  # Add librarian
            insert_librarian(lib_1)

        else:
            print('No Librarian was added')

    # search librarian

    elif interface == 'b':
        libs = get_librarian_by_name(input('Search Librarian by Last Name:'))
        print(libs)

    # Add/update/delete books

    elif(interface == 'c'):

        Add_books = input('Would you like to add books? YES/NO:')

        if Add_books == 'YES':
            book_1 = BOOKS('bookname', 'authorname', 'Identity', 'publicationcompany', 'rent', 'rentdate', 'username')
            insert_books(book_1)
        else:
            print('No book added')

    elif(interface == 'd'):
        available_books = get_available_books(input('Show available books(Type NO):'))
        print(available_books)

    elif(interface == 'f'):

        rented_books = get_rented_books(input('show rented books(Type YES):'))

    elif(interface == 'g'):
        Updatebook = input('Do you need to update rental information regarding a book? YES/NO:')

        if Updatebook == 'YES':
            upbook = update_books(input('Is the book rented? YES/NO:'), input('Date D-M-Y'), input('username'), input('ID:'))
            print('book was updated')
        else:
            print('rental info not updated')

    elif(interface == 'h'):

        Delete_Book = input('would you like to delete a book? YES/NO:')

        if Delete_Book == 'YES':

            delbook = del_books(input('bookid:'), input('BookName:'))
            print('Book was deleted succesfully')
        else:
            print('Deleting books is injurious to health')

    elif(interface == 'i'):

        New_USER = input('Are you a new USER?(YES/NO):')

        if New_USER == 'YES':
            cust_1 = USERS('first', 'last', 'USERname', 'password', 'contactdetails', 'fee', 'bookrented')
            insert_users(cust_1)
        else:
            olduser = old_user(input('username:'), input('password:'))
            print(olduser)

    elif(interface == 'j'):

        Delete_USER = input('would you like to delete your account? YES/NO:')

        if Delete_USER == 'YES':

            deluser = del_user(input('username:'), input('password:'))
            print('Your Account Has Been Deleted')
        else:
            print('User account was NOT deleted')

    elif(interface == 'k'):

        updateuser = update_user(input('newusername:'), input('newpassword:'), input('contact:'))

    interfaceloop = input('press a to return to main menu/npress b to quit')

connection.commit()
connection.close()
