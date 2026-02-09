#To map with real world scenarios, we started using object in code
#This is called Object Oriented Programming

#Before we were doing procedural coding and after that functional coding and followed bu OOP
#Function decreases redundancy and increases reusability

#Class is a blueprint for creating objects and objects are instances of class
#Constructor: All classes haev a function called __init__() which is always executed when the object is being initiated,
#constructor is invoked during the creation of object
#constructor always takes self as a parameter


class Student:
    def __init__(self,fullname):
        print("name is printing")
        self.name=fullname

#creating object

s1=Student("Fasi")
print(s1.name)

#The self parameter is a reference to the current instance of the class, and is used to access the variables that belongs to the class

class Car:
    # default constructor if not created by us then python will create one for us
    def __init__(self):
        pass

    #parameterized constructors
    def __init__(self,name,price):
        self.name = name  # instance attributes
        self.price = price

car=Car("Maruthi",2000)
print(car.name, car.price)

#Class Attributes & Instance Attributes




