#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Create a class Animal with a method make_sound. Then, create a subclass Dog that inherits from Animal and overrides the make_sound method. Allow the user to choose which animal's sound to make and demonstrate calling the make_sound method.

class Animal:
    def make_sound(self):
        return "Some generic sound"

class Dog(Animal):
    def make_sound(self):
        return "Bark"

animal_choice = input("Choose an animal (generic/dog): ")

if animal_choice == "generic":
    animal = Animal()
elif animal_choice == "dog":
    animal = Dog()
else:
    print("Invalid choice")
    animal = None

if animal:
    print(animal.make_sound())


# In[2]:


#Question:
#Create a class Person with an __init__ method to initialize the name and age attributes. Then, create a subclass Employee that inherits from Person and adds an additional attribute for the employee ID. Use super() to call the parent class's __init__ method. Prompt the user to input the details and create an Employee instance.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

name = input("Enter name: ")
age = int(input("Enter age: ")
employee_id = input("Enter employee ID: ")

employee = Employee(name, age, employee_id)

print(f"Name: {employee.name}, Age: {employee.age}, Employee ID: {employee.employee_id}")


# In[3]:


#Question:
#Create two base classes Flyer and Swimmer, each with a method move. Then, create a subclass Duck that inherits from both Flyer and Swimmer and demonstrate calling the move method based on user input.

class Flyer:
    def move(self):
        return "Flying"

class Swimmer:
    def move(self):
        return "Swimming"

class Duck(Flyer, Swimmer):
    def move(self):
        return "Swimming and Flying"

# Get user input
move_type = input("Choose movement type (fly/swim/both): ").strip().lower()

if move_type == "fly":
    movement = Flyer()
elif move_type == "swim":
    movement = Swimmer()
elif move_type == "both":
    movement = Duck()
else:
    print("Invalid choice")
    movement = None

if movement:
    print(movement.move())


# In[6]:


#Question:
#Write a program that prompts the user to enter a number and prints its square. Use a try and except block to handle non-numeric input gracefully.
try:
    number = float(input("Enter a number: "))
    print(f"The square of {number} is {number ** 2}")
except ValueError:
    print("That's not a valid number.")


# In[8]:


#Write a program that prompts the user to enter a numerator and a denominator and performs division. Use multiple except blocks to handle both non-numeric input and division by zero.

try:
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))
    result = numerator / denominator
    print(f"The result of the division is {result}")
except ValueError:
    print("That's not a valid number.")
except ZeroDivisionError:
    print("Division by zero is not allowed.")


# In[9]:


def divide (num, den):
    try:
        res = num / den
        return res 
    except ZeroDivisionError:
        print ("Divide Function: Divide by Zero Error")
        return 0
try:
    num = int(input ("Enter the numerator")) 
    den=int(input ('Enter the denominator'))
    result = divide (num, den)  
    print ("Result = ", result)

except ValueError:
           print ("main Block: Invalid Input" )

except ZeroDivisionError:
           print ("Main Block: Divide by Zero error")
print('End of Program ')


# In[10]:


#Define a custom exception class NegativeNumberError. Write a program that prompts the user to enter a positive number and raises this custom exception if the number is negative. Handle this exception using try and except blocks.

class NegativeNumberError(Exception):
    pass

def get_positive_number():
    try:
        number = float(input("Enter a positive number: "))
        if number < 0:
            raise NegativeNumberError("The number cannot be negative")
        return number
    except ValueError:
        print("That's not a valid number.")
        return None
    except NegativeNumberError as nne:
        print(f"Error: {nne}")
        return None

number = get_positive_number()
if number is not None:
    print(f"The number you entered is {number}")


# ##### 
