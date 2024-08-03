"""
Ejercicio
"""

# Incorrecto
class User:
  def __init__(self, username, password):
    self.username = username
    self.password = password
  
  def remove_database(self):
    pass

  def send_email(self):
    pass

# Correcto
class User:
  def __init__(self, username, password):
    self.username = username
    self.password = password

class Database:
  def remove_database(self):
    pass

class Email:
  def send_email(self, user):
    pass


"""
Extra
"""
class Library:

  def __init__(self):
    self.users = []
    self.books = []
    self.loans = []
  
  def register_user(self, name, id, email):
    new_user_data = {
      "name": name,
      "id": id,
      "email": email
    }
    self.users.append(new_user_data)
  
  def register_book(self, title, author, num_copies):
    new_book_data = {
      "title": title,
      "author": author,
      "num_copies": num_copies
    }
    self.books.append(new_book_data)
  
  def register_loan(self, user_id, book_title):
    for book in self.books:
      if book['title'] == book_title:
        book['num_copies'] -= 1
        new_loan_data = {
          "user_id": user_id,
          "book_title": book_title
        }
        self.loans.append(new_loan_data)
        return True
    return False
  
  def return_loan(self, user_id, book_title):
    for loan in self.loans:
      if loan['user_id'] == user_id and loan['book_title'] == book_title:
        self.loans.remove(loan)
        return True
    return False

# Correcto
class User:
  def __init__(self, name, id, email):
    self.name = name
    self.id = id
    self.email = email
  
class Book:
  def __init__(self, title, author, email):
    self.title = title
    self.author = author
    self.email = email

class Loan:
  def __init__(self):
    self.loans = []
  
  def register_loan(self, user, book):
    if book.copies > 0:
      book.copies -= 1
      new_loan_data = {
        "user_id": user.id,
        "book_title": book.title
      }
      self.loans.append(new_loan_data)
      return True
    return False
  
  def return_loan(self, user, book):
    for loan in self.loans:
      if loan["user_id"] == user.id and loan["book_title"] == book.title:
        self.loans.remove(loan)
        book.copies += 1
        return True
    return False

class Library:
  def __init__(self):
    self.users = []
    self.books = []
    self.loan_system = Loan()
  
  def register_user(self, user):
    self.users.append(user)
  
  def register_book(self, book):
    self.books.append(book)
  
  def register_loan(self, user, book):
    self.loan_system.register_loan(user, book)
  
  def return_loan(self, user, book):
    self.loan_system.return_loan(user, book)