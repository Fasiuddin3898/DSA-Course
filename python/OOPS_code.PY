#To map with real world scenarios, we started using object in code
#This is called Object Oriented Programming

#Before we were doing procedural coding and after that functional coding and followed bu OOP
#Function decreases redundancy and increases reusability

#Class is a blueprint for creating objects and objects are instances of class
#Constructor: All classes haev a function called __init__() which is always executed when the object is being initiated,
#constructor is invoked during the creation of object
#constructor always takes self as a parameter


# class Student:
#     def __init__(self,fullname):
#         print("name is printing")
#         self.name=fullname

#creating object

# s1=Student("Fasi")
# print(s1.name)

#The self parameter is a reference to the current instance of the class, and is used to access the variables that belongs to the class

class Car:
    # default constructor if not created by us then python will create one for us
    def __init__(self):
        print(f'print the value of self {self}')

    #parameterized constructors
    def __init__(self,name,price):
        self.name = name  # instance attributes
        self.price = price

car=Car("Maruthi",2000)
print(car.name, car.price)

#Class Attributes & Instance Attributes

class Student:
    def __init__(self,studentname,maths,science,english):
        self.name=studentname
        self.mat=maths
        self.scien=science
        self.engl=english
    @staticmethod
    def hello():
        print(f'Hai fasi i am static function will execute everytime')
    def average(self):
        self.hello()
        print((self.mat+self.scien+self.engl)//3)


s1=Student("fasi",2,3,4)
s1.average()
s1.hello()

#Abstraction
class Car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False
    def start(self):
        self.acc=True
        self.clutch=True
        print(f'Car has started')

car=Car()
car.start()

class Account:
    def __init__(self,balance,acc_no):
        self.bal=balance
        self.acc=acc_no
    def debit(self,withdraw):
        self.bal=self.bal-withdraw
        print(f'remaining amount after with draw is {self.bal}')
    def credit(self,credited):
        self.bal=self.bal+credited
        print(f'remaining amount after credit is {self.bal}')
    def balance(self):
        print(f'remaing balance is {self.bal}')

account=Account(100,1234)
account.debit(50)
account.credit(100)
account.balance()

#Private attribute and method code
class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass

    def reset_password(self):
        print(f'password {self.__acc_pass}')

    def __hello(self):  #can not be accessed outside the class
        print(f'welcome')

    def welcome(self):
        self.__hello()

acc1=Account(12345,"abcde")
acc1.reset_password() #this will print the password
acc1.welcome()
# acc1.__hello()
# print(acc1.__acc_pass) #this will throw the error

#Inheritance
class Car:
    @staticmethod
    def start():
        print(f'car started..')

    @staticmethod
    def stop():
        print(f'car stopped')

class ToyotaCar(Car):
    def __init__(self,name):
        self.name=name

car1=ToyotaCar("fortuner")
car2=ToyotaCar("prius")
car1.start()
car2.stop()

class Car1:
    def __init__(self,type):
        self.type=type
    @staticmethod
    def start():
        print(f'car started..')

    @staticmethod
    def stop():
        print(f'car stopped')

class ToyotaCar1(Car1):
    def __init__(self,brand,type):
        super().start()
        super().__init__(type)
        self.brand=brand
 

cara=ToyotaCar1("prius","electric")
print(cara.type)


class Person:
    name="Anonymous"
    def changename(self,name):
        self.__class__.name=name
    def changename2(self,name):
        Person.name=name

    @classmethod
    def changeName3(cls,name):  #cls is not self it is refering to class
        cls.name=name

p1=Person()
p1.changename("fasi")
print(p1.name)
print(Person.name)
p1.changename2("uddin")
print(p1.name)
print(Person.name)
p1.changeName3("fasiuddin")
print(p1.name)
print(Person.name)

class Student:
    def __init__(self,phy,scie,math):
        self.phy=phy
        self.scie=scie
        self.math=math
        self.percentage=str((self.phy+self.scie+self.math)/3)+"%"
    @property
    def percentage1(self):
        return str((self.phy+self.scie+self.math)/3)+"%"


stu1=Student(99,98,97)
print(stu1.percentage)
stu1.math=100
print(stu1.math)
print(stu1.percentage)
print(stu1.percentage1)


#Polymorphism
class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def showNumber(self):
        print(self.real,"i +",self.img,"j")

    def addNumber(self,num2):
        new_real=self.real+num2.real
        new_real=self.img+num2.img
        return Complex(new_real,new_real)
    
    def __add__(self,num2):
        new_real=self.real+num2.real
        new_real=self.img+num2.img
        return Complex(new_real,new_real)


num1=Complex(1,3)
num1.showNumber()

num2=Complex(4,5)
num2.showNumber()

num3=num1.addNumber(num2)
num3.showNumber()

num4=num1+num2
num4.showNumber()


class Circle:
    def __init__(self,radius):
        self.r=radius

    def area(self):
        print(f'area of circle {3.14*(self.r**2)}')

    def permimeter(self):
        print(f'permimeter of a circle {2*3.14*self.r}')

c1=Circle(3)
c1.area()
c1.permimeter()


class Employee:
    def __init__(self,role,department,salary):
        self.role=role
        self.department=department
        self.salary=salary

    def showDetails(self):
         print(f'current employee role is {self.role} amd works in {self.department} has {self.salary} salary')

class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Software Engineer","BE",40000)

e1=Employee("SE","BE",40000)
e1.showDetails()

e2=Engineer("fasi",25)
e2.showDetails()

class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price

    def __gt__(self,order2):
        if self.price>order2.price:
            print(f'order 1 is greater then order 2')
            return True
        else:
            print("order 2 is greater then order 1")
            return False

o1=Order("any1",20)
o2=Order("any2",10)
print(o1>o2)


#getter and setter methods usage
class Human:
    def __init__(self,age):
        self.__age=age # private variable

    #getter
    def get_age(self):
        return self.__age
    
    #setter
    def set_age(self,age):
        if age>0:
            self.__age=age
        else:
            print("Age must be positive")

p = Human(25)

# using getter
print(p.get_age())

# using setter
p.set_age(30)
print(p.get_age())

p.set_age(-5)   # invalid

#Modren way
class Person:

    def __init__(self, age):
        self.__age = age

    # Getter
    @property
    def age(self):
        return self.__age

    # Setter
    @age.setter
    def age(self, value):
        if value > 0:
            self.__age = value
        else:
            print("Age must be positive")


p = Person(25)

print(p.age)   # getter
p.age = 35     # setter
print(p.age)

p.age = -5     # invalid
