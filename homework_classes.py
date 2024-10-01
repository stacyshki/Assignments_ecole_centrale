# TASK 1


class Rectangle:
  
  def __init__(self, length : int, width : int):
    self.length = length
    self.width = width
  
  def calculate_area(self):
    return self.length * self.width
  
  def calculate_perimeter(self):
    return (self.length + self.width) * 2


# Example

rectangle_1 = Rectangle(4, 5)
rectangle_2 = Rectangle(654, 321)
print(rectangle_1.calculate_area())
print(rectangle_2.calculate_perimeter(), end='\n\n')


# TASK 2


class Person:
  
  def __init__(self, name : str, age : int):
    self.__name = name
    self.__age = age
  
  def get_name(self):
    return self.__name
  
  def get_age(self):
    return self.__age
  
  def set_name(self, new_name : int):
    self.__name = new_name
  
  def set_age(self, age : int):
    self.__age = age


# Example

person = Person('Viktor', 17)

print(person.get_name())
print(person.get_age(), end='\n\n')
person.set_age(18)
person.set_name('Zhao')
print(person.get_name())
print(person.get_age(), end='\n\n')


# TASK 3


class Vehicle:
  
  def __init__(self, make : str, model : str):
    self.make = make
    self.model = model


class Motorcycle(Vehicle):
  
  def __init__(self, make : str, model : str):
      super(Motorcycle, self).__init__(make, model)
  
  def display_info(self):
    print(f'{self.make} - is the make of your car')
    print(f'{self.model} - is the model of your car')


class Car(Vehicle):
    
  def __init__(self, make : str, model : str):
    super(Car, self).__init__(make, model)
  
  def display_info(self):
    print(f'{self.make} - is the make of your motorcycle')
    print(f'{self.model} - is the model of your motorcycle')


# Example

car = Car('Audi', 'RS6')
motorcycle = Motorcycle('Harley', 'Davidson')

car.display_info()
print()
motorcycle.display_info()
print()


# TASK 4


class Library:
  
  def __init__(self, name : str):
    self.name = name
    self.books = []
  
  def add_books(self, book : object):
    self.books.append((book.title, book.author))
  
  def display_library(self):
    print(*self.books)


class Book:
  
  def __init__(self, title : str, author : str):
    self.title = title
    self.author = author


# Example

library_berlin = Library('Berlin Central Library')
book_alg = Book('Grokking Algorithms', 'Aditya Y. Bhargava')
book_cs = Book('Computer Science An Overview', 'J. Glenn Brookshear')
library_berlin.add_books(book_alg)
library_berlin.add_books(book_cs)
library_berlin.display_library()
print()


# TASK 5

class University:
  
  def __init__(self, name : str, departments : tuple):
    self.name = name
    self.departments = departments


class Department:
  
  def __init__(self, name : str):
    self.name = name
    self.students = []


# Example

department_cs = Department('Computer Science')
department_cs.students.append('Viktor Korotkov')
department_cs.students.append('Zhao Shitao')
department_ml = Department('Machine learning')
department_ml.students.append('Viktor Korotkov')
department_ml.students.append('Sergey Mavrodi')

departments = (department_cs,department_ml)
berlin_university = University('Berlin', departments)

print(department_ml.name)
print(department_ml.students)
print(berlin_university.name)
print(berlin_university.departments, end='\n\n') # objects tuple


# TASK 6


class Teacher:
  
  def __init__(self, name : str):
    self.name = name
    self.students = []


class Student:
  
  def __init__(self, name : str, age : int):
    self.name = name
    self.age = age


# Example

teacher = Teacher('Leo Tolstoy')
student_1 = Student('Viktor', 17)
student_2 = Student('Dmitri', 19)
teacher.students.append(student_1)
teacher.students.append(student_2)

print(student_2.name)
print(student_2.age)
print(teacher.name)
print(teacher.students, end='\n\n') # objects list


# TASK 7

from math import pi


class Shape:
  
  def __init__(self, length : float):
    self.length = length
  
  def area(self):
    return 1 * self.length


class Rectangle(Shape):
  
  def __init__(self, length : float, width : float):
    super(Rectangle, self).__init__(length)
    self.width = width
  
  def area(self):
    return self.length * self.width


class Circle(Shape):
  
  def __init__(self, radius : float, pi : float):
    self.radius = radius
    self.pi = pi
  
  def area(self):
    return self.pi * self.radius ** 2


# Example

rectangle = Rectangle(20, 7)
circle = Circle(4, pi)

print(rectangle.area())
print(circle.area())