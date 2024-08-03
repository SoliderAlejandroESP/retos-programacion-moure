"""
Ejercicio
"""

class Singleton:

  _instance = None

  def __new__(cls):
    if not cls._instance:
      cls._instance = super().__new__(cls)
    return cls._instance

singleton1 = Singleton()
print(singleton1)
singleton2 = Singleton()
print(singleton2)

print(singleton1 is singleton2)


"""
Extra
"""

class UserSession:

  _instance = None

  id = None
  username = None
  name = None
  email = None

  def __new__(cls):
    if not cls._instance:
      cls._instance = super(UserSession, cls).__new__(cls)
    return cls._instance
  
  def set_user(self, id, username, name, email):
    self.id = id
    self.username = username
    self.name = name
    self.email = email
  
  def get_user(self):
    return f"id: {self.id}, username: {self.username}, name: {self.name}, email: {self.email}"
  
  def clear_user(self):
    self.id = None 
    self.username = None 
    self.name = None
    self.email = None

s1 = UserSession()
print(s1)
s2 = UserSession()
print(s2)
print(s1 is s2)

s1.set_user(23, "shadow", "Alejandro", "solideralejandro@gmail.com")
print(s1.get_user())
print(s2.get_user())
s2.clear_user()
print(s1 is s2)
print(s1.get_user())