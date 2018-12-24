import datetime


class librarian:

    def __init__(self, first, last, contact):
        self.first = input('Librarian firstname:')
        self.last = input('Librarian lastname:')
        self.contact = int(input('Librarian Number:'))


class BOOKS(librarian):

    def __init__(self, bookname, authorname, Identity, publicationcompany, rent, rentdate, username):

        # super().__init__(self)
        self.bookname = input('Bookname:')
        self.authorname = input('Authorname:')
        self.Identity = int(input('IDnumber:'))
        self.publicationcompany = input('PublicationcompanyName:')

        self.Rent = input('Rent Book YES/NO:')
        self.rentdate = datetime.datetime.strptime(input('Day-Month-Year:'), '%d-%M-%Y')
        self.username = input('username:').upper()


class USERS(BOOKS):

    def __init__(self, first, last, USERname, password, contactdetails, fee, bookrented):

        # super.().__init__(self)
        self.first = input('Firstname:')
        self.last = input('Lastname:')
        self.USERname = input('Create Username:')
        self.password = input('Create Password:')
        self.contactdetails = input('contactdetails:')
        self.fee = input('Fee:')
        self.bookrented = int(input('bookid:'))
