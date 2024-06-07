#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


#Q1: Write a Python class named Book that has the following attributes: title, author, and pages. Create an instance of this class by taking user input for the attributes and then print out its attributes. question by revanth


class Book:
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
        
title = input("enter title: ")
author = input("enter author name: ")
pages = int(input("no.of pages: "))

book = Book(title,author,pages)
print(f"Title: {book.title}, Author: {book.author},Pages: {book.pages}")



# In[5]:


#Create classes Battery and ElectricCar where ElectricCar has an instance of Battery. Implement a method in Battery to
#display the battery size and call this method from an instance of ElectricCar. Take user input for the attributes.



class Battery:
    def __init__ (self,size):
        self.size = size
    def display_battery_size(self):
        print(f"Battey size : {self.size}kw")
class ElectricCar:
    def __init__ (self,make,model,batterysize):
        self.make = make
        self.model = model
        self.batterysize = Battery(batterysize)
    def display_info(self):
        print(f"Car make : {self.make}, Car model : {self.model}")
        self.batterysize.display_battery_size()    
        
        
make = input("make of car: ")
model = input("model of car: ")
batterySize = int(input("ba5ttery size: "))

rev_car = ElectricCar(make,model,batterySize)
rev_car.display_info()


# In[11]:


#Create an abstract class Shape with an abstract method area. Then, create two subclasses Rectangle and Circle that implement the area method. Create instances using user input and print their areas.

from abc import ABC , abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
class Rectangle(Shape):
    def __init__(self,breadth,length):
        self.length = length
        self.breadth = breadth
        
    def area(self):
        return self.length * self.breadth
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
        
    def area(self):
        return math.pi* self.radius **2
    
length = int(input("length of rectangle: "))
breadth = int(input("breadth of rectangle: "))

rectangle = Rectangle(length,breadth)

radius = int(input("enter radius: "))
circle = Circle(radius)

print("length of rectangle", rectangle.length, "beadth of rectangle", rectangle.breadth ,
     "area of rectangle " , rectangle.area())
print("Circle with radius", circle.radius, "has an area of:", circle.area())


# In[12]:


#Q: Write a Python class Vector that represents a vector in a 2-dimensional space. Implement the __add__ method to overload the + operator so that two vectors can be added together. Demonstrate this by creating two instances of the Vector class and adding them together.

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

x1 = float(input("Enter the x coordinate of the first vector: "))
y1 = float(input("Enter the y coordinate of the first vector: "))
vector1 = Vector(x1, y1)

x2 = float(input("Enter the x coordinate of the second vector: "))
y2 = float(input("Enter the y coordinate of the second vector: "))
vector2 = Vector(x2, y2)

resultant_vector = vector1 + vector2
print("The sum of the vectors is:", resultant_vector)


# In[13]:


#: Write a Python class TemperatureConverter that contains a static method celsius_to_fahrenheit to convert a temperature from Celsius to Fahrenheit and another static method fahrenheit_to_celsius to convert a temperature from Fahrenheit to Celsius. Demonstrate these methods by taking user input for a temperature in Celsius and Fahrenheit and converting them.

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = TemperatureConverter.celsius_to_fahrenheit(celsius)
print(celsius, "Celsius is equal to", fahrenheit, "Fahrenheit")

fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = TemperatureConverter.fahrenheit_to_celsius(fahrenheit)
print(fahrenheit, "Fahrenheit is equal to", celsius, "Celsius")


# In[ ]:





# In[ ]:





# In[ ]:




