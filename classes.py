# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object
class User_fba:

  def __init__(self, name, email, age):
    self.name = name
    self.email = email
    self.age = age
    
    self._private = 1000

  def greeting(self):
      return f'My name is {self.name} and I am {self.age}'

  def has_birthday(self):
      self.age += 1
 
  def print_encap(self):
      print(self._private)

class Customer(User_fba):
  
  def __init__(self, name, email, age):
      User_fba.__init__(self, name, email, age) 
      self.name = name
      self.email = email
      self.age = age
      self.balance = 0

  def set_balance(self, balance):
      self.balance = balance

  def greeting(self):
      return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'


feridun = User_fba('feridun arik', 'feridun@gmail.com', 21)

berkin = Customer('berkin aarik', 'berkin@yahoo.com', 22)

berkin.set_balance(500)
print(berkin.greeting())

feridun.has_birthday()
print(feridun.greeting())

feridun.print_encap()
feridun._private = 800 
feridun.print_encap()

berkin.print_encap() 
berkin._private = 600
berkin.print_encap()

feridun.print_encap()
