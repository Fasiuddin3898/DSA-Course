What is python..?
Python is High-Level, interpreted, Dynamically typed, Object-Oriented programming languauge, which supports
multi paradigms like OOPs, Functional, Procedural

Mutable: can change after creation example:list,dict,set
Immutable: can not be changed after creation:int,float,string,tuple
a = [1, 2]
a.append(3)  # allowed
b = "hello"
b[0] = "H"  # ❌ error

what is list:ordered mutable collection ex:lst=[1,2,3]
important list methods
lst.append(x) #adds element at last
lst.insert(i,x) #inserts element at i index
lst.remove(x) #removes the first occurance of  value from list
lst.pop() #removes last element
lst.sort() #sort the list
lst.reverse() #reverse the list
len(lst) # returns the length of list

List Comprehension:is a concise, single-line way to create a new list by
iterating over an existing iterable(like a list,tuple,or range) and 
optinally applying a condition to filter elements
example
squares=[x*x for x in range(5)]
with condition
even=[x for x in range(10) if x%2 ==0]

shallow Copy vs Deep Copy
Shallow Copy:Creates a new object but reference the originals nested elements
if you modify the nested element in the copy,it will change in the original because
they share the same memory address for the inner item
Deep Copy:Creates a completely indepenedent clone of the object and all its nested 
elements.It recursively copies every level,so changes in the deep copy
never affect the original.
Comparison Table
Feature 	    Shallow Copy (copy.copy())	                Deep Copy (copy.deepcopy())
Independence	Only the outer container is independent.	Entire structure is fully independent.
Nested Objects	References are shared.                  	Nested objects are recursively cloned.
Performance	    Faster; uses less memory.                	Slower; uses more memory.
Best Use Case	Flat lists or when sharing data is okay.	Complex nested structures where you need a "true" backup.

example
import copy
original=[[1,2],[3,4]]
shallow=copy.copy(original)
deep=copy.deepcopy(original)
shallow[0][0]='x'
print(original) # Output: [['X', 2], [3, 4]] (Original is affected!)
print(deep)     # Output: [[1, 2], [3, 4]]     (Deep copy is safe)

Reverse a list lst[::-1]
Find duplicates
seen = set()
dup = set()
for num in lst:
    if num in seen:
        dup.add(num)
    else:
        seen.add(num)

What is Tuple:A tuple is a buil-in python data structure used to store A
collection of items in a single varaible.it is very simillar to a lit, but 
with one critical difference is it is Immutable
Key Characteristics
Immutable: Once created, you cannot change, add, or remove elements.
Ordered: Items have a defined order that will never change.
Allows Duplicates: Since tuples are indexed, they can contain multiple identical values.
Heterogeneous: A single tuple can store multiple data types (e.g., strings, integers, and booleans all in one). 
Why use Tuple?
Protect data
Used as dictionary keys
Faster iteration
my_tuple = ("apple", "banana", "cherry")
# Mixed Data Types
mixed_tuple = ("Alice", 25, True)
# Single Item Tuple (IMPORTANT: must have a trailing comma)
single_item = ("apple",) 
# Without the comma, Python treats it as a string: ("apple")

In a Python interview, you should explain that tuples are faster than lists because their immutability allows for several low-level optimizations in the CPython interpreter: 
1. Lower Memory Overhead (No Over-allocation) 
Lists are dynamic; they over-allocate extra memory slots to make future append() operations efficient.
Tuples are fixed-size; Python allocates exactly the memory needed for the elements at the time of creation, making them more compact. 
Stack Overflow
Stack Overflow
 +4
2. Single Memory Block Allocation
Lists are stored in two separate memory blocks: one for the list object and another for the data array.
Tuples store everything in a single contiguous block of memory. This reduces the number of memory allocations and improves "cache locality," making access slightly faster. 
Stack Overflow
Stack Overflow
 +3
3. Constant Folding (Compiler Optimization) 
When you define a tuple of constants (e.g., x = (1, 2, 3)), the Python compiler can pre-compute it and store it as a single constant in the bytecode.
A list (e.g., [1, 2, 3]) must be reconstructed from scratch every time that line of code runs because lists are mutable and could have been changed elsewhere. 

Dictionary:key-value pair, Mutable, Keys must be Immutable
d = {"a": 1, "b": 2}
d.keys()
d.values()
d.items()
d.get("a)
d.pop("a)
squares = {x: x*x for x in range(5)}
How Dictionary Works Internally?
Uses Hash Table
O(1) average time complexity
Merge Dictionaries
d1.update(d2) 
d3 = d1 | d2

What is Set:Unordered, Unique elements, Mutable
s={1,2,3}
Operations:
a | b # union
a & b # intersection
a - b # difference

Operators:In python operators are special symbols or keywords used to perform computations and variables.The values being opetrated on are operands.
1.Arithmetic Operators:+,-,*,/,//,%,**(exponention)
2.Assignment Operators:x=5,x+=5,x*=5
3.Comparison Operators:==,!=,>,<,>=,<=
4.Logical Operators:and,or,not
5.Special Operators:
 a.Identity Operators(is,is not):Check if two variables point to the same object in memory, not just the same value
 list_a = [1, 2, 3]
 list_b = list_a          # Both point to the same list in memory
 list_c = [1, 2, 3]       # A new list with the same values
 print(list_a is list_b)  # True  (Same object)
 print(list_a is list_c)  # False (Different objects, even if values are identical)
 print(list_a == list_c)  # True  (Values are the same)
 b.Membership Operators(in,not in):Check if the value exits within a sequence like a list,string or tuple
6.Bitwise Operators:Perform operations on binary digits (bits) of integers:&(AND),|(OR),^(XOR),~(NOT),<<(Left Shift),>>(Right Shift)

Functions:can be defined as reusable component
Type of Arguments:
1.Positional Argumenst:Values are matched to parameters based strictly on the order in which they are passed
def describe_pet(animal,name):
    print(f"I have a {animal} named {name}")
describe_pet("dog","Buddy")

2.Keyword Arguments:You pass the argument by explicitly naming the parameter(name=value).This makes the order irrelevent and increase the redability
describe_pet(name="Buddy",animal="dog")

3.Default Arguments:These have a predefined value assigned in the function defination.They become optional,if you don't provide a value the default is used.
def greet(name, msg="hello"):
    print(f'{msg},{name}')
greet("Alice")
greet("Bob","Hi")

4.Variable-Length Arguments:Used when you don't know in advance how many arguments will be passed
a.Arbitrary Positinal Arguments(*args):Collects extra positional arguments into a tuple
def sum_a11(*numbers):
    return sum(numbers)
print(sum_all(1,2,3,4)) #output 10
b.Arbitrary Keyword Arguments(**kwargs):Collects extra keyword argumenst into a dictionary
def show_info(**data):
    for key,value in data.items():
        print(f"{key},{value}")
show_info(name="fasi",age=26,course="python")

**Important Rule when we mix all this in a function order to follow:Positional -> *args -> Default -> **kwargs

**Lambda Function:A lambda function is a small,anonymous function in python that is defined without a name using the lambda leyword.Unlike regular functions defined with def,lambda 
functions are limited to a single expression and are typically used for short-term,throwaway

Syntax lambda arguments: expression

1.Square of a number
square= lambda x: x**2
ans=square(4) # output:16

2.Using the filter() find even numbers:Lambda function is frequently used to filter items in a list based on a condition.
numbers=[1,2,3,4,5,6,7,8,9,10]
even_numbers=list(filter(lambda x: x%2==0,numbers))
print(even_numbers) #output [2,4,6,8,10]

3.Using with map():Apply an operation to every item in a list
names=["alice","bob","fasi"]
captalized=list(map(lambda x:x.upper(),names))
print(captalized) # output ["ALICE","BOB","FASI"]

4. Custom Sorting:Sort a list of tuples by the second element (e.g., age): 
students = [("Alice", 25), ("Bob", 22), ("Charlie", 28)]
sorted_students = sorted(students, key=lambda student: student[1])
print(sorted_students)  # Output: [('Bob', 22), ('Alice', 25), ('Charlie', 28)]

**Closure:A closure in Python is a nested function that remembers and can access the variables from its outer(enclosing) function scope, even after the outer function has finished exexuting.
def outer(x):
    def inner(y):
        return x+y
add5=outer(5)
print(add5(10)) #output 15
When clouser is used
1.Data Hiding:They provide a simple way to hide data from global scope,simlar to private variables in class
2.Function Factories:You can use them to generate many specialized functions with different preset behaviours
3.Stateful Functions:They can track state between calls(e.g a counter) without uising a global variables
4.Decorators:Python's decorators are essentially advanced implementation of closures

**Decorator:Decorator is a function that takes another function as argument and return a function
A Decorator is a design pattern in Python that allows you to wrap another function or class to extend or modify its behaviour without changing its original source code.
def decorator(func):
    def wrapper():
        print(f'transaction statrted')
        func()
        print(f'transcation ended')
    return wrapper

def hello():
    print(f'..Executing all steps on transaction..')

hello1=decorator(hello)
hello1()

@decorator
def hello2():
    print(f'example execute all my transactions')

hello2()




