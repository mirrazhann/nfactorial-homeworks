from datetime import datetime, timedelta
import math
import random

"""
Exercise 1:
Create a Pizza class that could have ingredients added to it. Raise an error if an attempt is made to add a duplicate ingredient.
"""
class Pizza:
    def __init__(self):
        self.ingredients = []
    
    def add_ingredient(self, ingredient):
        if ingredient in self.ingredients:
            raise ValueError(f"{ingredient} was added early")
        self.ingredients.append(ingredient)


"""
Exercise 2:
Create an Elevator class with methods to go up, go down, and get the current floor. The elevator should not be able to go below the ground floor (floor 0).
"""
class Elevator:
    def __init__(self):
        self.min_floor = 0
        self.current_floor = 0

    def go_up(self):
        self.current_floor +=1

    def go_down(self):
        if self.current_floor > 0:
            self.current_floor -= 1

    def get_current_floor(self):
        return self.current_floor


"""
Exercise 3:
Create a class Stack with methods to push, pop, and check if the stack is empty. Raise an exception if a pop is attempted on an empty stack.
"""
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError(f"Empty stack")
        else:
            return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0


"""
Exercise 4:
Design a BankAccount class with methods to deposit, withdraw, and check balance. Ensure that an account cannot go into a negative balance.
"""
class BankAccount:
    def __init__(self, initial_balance):
        self.ballance = initial_balance

    def deposit(self, amount):
        self.ballance += amount

    def withdraw(self, amount):
        if self.ballance - amount >= 0:
            self.ballance -= amount
        else:
            raise ValueError('The ballance can not be negative')

    def check_balance(self):
        return self.ballance


"""
Exercise 5:
Create a class Person with attributes for name and age. Implement a method birthday that increases the person's age by one. Raise an exception if an age less than 0 is entered.
"""
class Person:
    def __init__(self, name, age):
        if age < 0:
            raise ValueError('Invalide age')
        else:
            self.name = name
            self.age = age

    def birthday(self):
        self.age += 1

    


"""
Exercise 6:
Create an Animal base class and a Dog and Cat derived classes. Each animal should have a sound method which returns the sound they make.
"""
class Animal:
    def sound(self):
        return ""

class Dog(Animal):
    def sound(self):
        return "Woof"

class Cat(Animal):
    def sound(self):
        return "Meow"


"""
Exercise 7:
Design a class Calculator with static methods for addition, subtraction, multiplication, and division. Division method should raise a ZeroDivisionError when trying to divide by zero.
"""
class Calculator:
    @staticmethod
    def add(x, y):
        return x+y

    @staticmethod
    def subtract(x, y):
        return x-y

    @staticmethod
    def multiply(x, y):
        return x*y

    @staticmethod
    def divide(x, y):
        if y == 0:
            raise ZeroDivisionError('Error! y == 0')
        else:
            return x/y


"""
Exercise 8:
Create a class `Car` with attributes for speed and mileage. Raise a ValueError if a negative value for speed or mileage is entered.
"""
class Car:
    def __init__(self, speed, mileage):
        if speed < 0:
            raise ValueError('Speed can not be negative')
        elif mileage < 0:
            raise ValueError('Mileage can not be negative')
        else:
            self.speed = speed
            self.mileage = mileage



"""
Exercise 9:
Create a Student class and a Course class. Each Course can enroll students and print a list of enrolled students.
"""
class Student:
    def __init__(self, name):
        self.name = name

class Course:
    def __init__(self):
        self.students = []

    def enroll(self, student):
        self.students.append(student)

    def print_students(self):
        print(self.students)


"""
Exercise 10:
Create a Flight class with a destination, departure time, and a list of passengers. Implement methods to add passengers, change the destination, and delay the flight by a certain amount of time.
"""
class Flight:
    def __init__(self, destination, departure):
        self.destination = destination
        self.departure = departure
        self.passengers = []

    def add_passenger(self, passenger):
        self.passengers.append(passenger)

    def change_destination(self, new_destination):
        self.destination = new_destination

    def delay(self, delay_time):
        time_obj = datetime.strptime(self.departure, "%H:%M")
        time_plus_one_hour = time_obj + timedelta(hours=delay_time)
        self.departure = time_plus_one_hour.strftime("%H:%M")


"""
Exercise 11:
Create a Library class with a list of Book objects. The Book class should have attributes for title and author. The Library class should have methods to add books and find a book by title.
"""
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_by_title(self, title):
        for i in self.books:
            if i.title == title:
                return i
        raise ValueError("Not found book by title")


"""
Exercise 12:
Design a class Matrix that represents a 2D matrix with methods for addition, subtraction, and multiplication. Implement error handling for operations that are not allowed (e.g., adding matrices of different sizes).
"""
class Matrix:
    def __init__(self, matrix):
        if self.check_matrix(matrix) != True:
            raise ValueError('Invalid matrix')
        else:
            self.matrix = matrix

    def add(self, other):
        if self.check_matrix(other.matrix) != True:
            raise ValueError('Invalid other matrix')
        else:
            result = [[0 for _ in range(len(self.matrix[0]))] for _ in range(len(self.matrix))]
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    result[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Matrix(result)

    def subtract(self, other):
        if self.check_matrix(other.matrix) != True:
            raise ValueError('Invalid other matrix')
        else:
            result = [[0 for _ in range(len(self.matrix[0]))] for _ in range(len(self.matrix))]
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    result[i][j] = self.matrix[i][j] - other.matrix[i][j]
        return Matrix(result)

    def multiply(self, other):
        if self.check_matrix(other.matrix) != True:
            raise ValueError('Invalid other matrix')
        else:
            result = [[0 for _ in range(len(self.matrix[0]))] for _ in range(len(self.matrix))]
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    result[i][j] = self.matrix[i][j] * other.matrix[i][j]
        return Matrix(result)

    def check_matrix(self, matrix):
        if not isinstance(matrix, list) or not matrix:
            return False 
        if len(matrix) != 2:
            return False
        if not all(isinstance(row, list) and len(row) == len(matrix[0]) and len(row) == 2 for row in matrix):
            return False
        return True


"""
Exercise 13:
Create a class Rectangle with attributes for height and width. Implement methods for calculating the area and perimeter of the rectangle. Also, implement a method is_square that returns true if the rectangle is a square and false otherwise.
"""
class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2

    def is_square(self):
        return self.height == self.width

# rectangle = Rectangle(3, 4) 
# print(rectangle.area())

"""
Exercise 14:
Design a class Circle with attributes for radius. Implement methods for calculating the area and the circumference of the circle. Handle exceptions for negative radius values.
"""
class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Error! Negative radius!")
        else:
            self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def circumference(self):
        return 2 * math.pi * self.radius
    
# circle = Circle(5)
# print(circle.area(), 78.53981633974483)

"""
Exercise 15:
Design a class Triangle with methods to calculate the area and perimeter. Implement error handling for cases where the given sides do not form a valid triangle.
"""
class Triangle:
    def __init__(self, side_a, side_b, side_c):
        if side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a:
            self.a = side_a
            self.b = side_b
            self.c = side_c
        else:
            raise ValueError('Error! Invalid datas')

    def area(self):
       p = self.perimeter() / 2
    #    print(p, self.perimeter())
       return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def perimeter(self):
        return self.a + self.b + self.c


"""
Exercise 16:
Design a class Triangle with methods to calculate the area and perimeter. Implement error handling for cases where the given sides do not form a valid triangle.
"""
class AbstractShape:
    def area(self):
        raise NotImplementedError("Abstract class")


    def perimeter(self):
        raise NotImplementedError("Abstract class")


class Circle(AbstractShape):
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Error! Negative radius!")
        else:
            self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def circumference(self):
        return 2 * math.pi * self.radius

class Rectangle(AbstractShape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2

    def is_square(self):
        return self.height == self.width

class Triangle(AbstractShape):
    def __init__(self, side_a, side_b, side_c):
        if side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a:
            self.a = side_a
            self.b = side_b
            self.c = side_c
        else:
            raise ValueError('Error! Invalid datas')

    def area(self):
       p = self.perimeter() / 2
    #    print(p, self.perimeter())
       return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def perimeter(self):
        return self.a + self.b + self.c

"""
Exercise 17:
Create a MusicPlayer class that contains a list of songs and methods to add songs, play a song, and skip to the next song. Also implement a method to shuffle the playlist.
"""
class MusicPlayer:
    def __init__(self):
        self.playlist = []
        self.current_index = 0
        self.current_song = None
        

    def add_song(self, song):
        self.playlist.append(song)

    def play_song(self):
        if not self.playlist:
            return None

        self.current_song = self.playlist[self.current_index]

    def next_song(self):
        if not self.playlist:
            return None

        if(self.current_index + 1 <= len(self.playlist)-1):
            self.current_index = self.current_index + 1
            self.current_song = self.playlist[self.current_index]

    def shuffle(self):
        random.shuffle(self.playlist)
        self.current_index = 0
        self.current_song = self.playlist[self.current_index]


"""
Exercise 18:
Design a Product class for an online store with attributes for name, price, and quantity. Implement methods to add stock, sell product, and check stock levels. Include error handling for attempting to sell more items than are in stock.
"""
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def add_stock(self, quantity):
        self.quantity += quantity

    def sell(self, quantity):
        if self.quantity - quantity < 0:
            raise ValueError("Error! Negative stock")
        else:
            self.quantity -= quantity

    def check_stock(self):
        return self.quantity


"""
Exercise 19:
Create a VideoGame class with attributes for title, genre, and rating. Implement methods to change the rating, change the genre, and display game details.
"""
class VideoGame:
    def __init__(self, title, genre, rating):
        self.title = title
        self.genre = genre
        self.rating = rating

    def change_rating(self, rating):
        self.rating = rating

    def change_genre(self, genre):
        self.genre = genre

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Genre: {self.genre}")
        print(f"TRating: {self.rating}")


"""
Exercise 20:
Create a School class with a list of Teacher and Student objects. Teacher and Student classes should have attributes for name and age. The School class should have methods to add teachers, add students, and print a list of all people in the school.
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Teacher(Person):
    pass

class Student(Person):
    pass

class School:
    def __init__(self):
        self.students = []
        self.teachers = []

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_student(self, student):
        self.students.append(student)

    def print_all(self):
        print(self.students)
        print(self.teachers)


"""
Exercise 21:
Design a Card class to represent a playing card with suit and rank. Then design a Deck class that uses the Card class. The Deck class should have methods to shuffle the deck, deal a card, and check the number of remaining cards.
"""
# class Card:
#     def __init__(self, suit, rank):
#         self.suit = suit
#         self.rank = rank

# class Deck:
#     def __init__(self):
#         pass

#     def shuffle(self):
#         pass

#     def deal(self):
#         pass

#     def count(self):
#         pass
