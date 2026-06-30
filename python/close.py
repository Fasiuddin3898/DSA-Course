import time
# def multiplier(n):
#     def multiply(x):
#         print(f'ans {n*x}')
#     return multiply

# double=multiplier(2)
# triple = multiplier(3)

# print(f'double {double}') # ans 20 is output

# print(f'main_ans {double(10)}') #None is output because 

# print(f'triple value is {triple(10)}')

# To understand closer the defination is inner function remmebers the outer function variables even after the outer
# function finishes the execution
# In above example when we call the outer function which is multiplier(2) so it returns the inner function the execution is done
# but still it remembers what is the value of n which is 2 and now when we call the inner function, the returned value is the way 
# of calling inner function so we call it with double(10) now it calls the inner function the inner function already know the n is 2 
# so it directly multiplies 10 with 2 


# Now a decorator is a function which takes another function and extends its behaviour
# Lets say we want to know how much does a function is taking to execute we write 

# def sq(nums):
#     t1=time.time()
#     for i in nums:
#         print(f'Squares {i**i}')

#     t2=time.time()

#     print(f'Time taken for squares to execute {t2-t1}')

# nums=[1,2,3,4]
# sq(nums)

# Suppose we also want timing for:

# square()
# factorial()
# sum_numbers()

# We'd duplicate timing code everywhere.

# Decorator solve this 

def timer(func):

    def wrapper(args):
        start=time.time()
        result=func(args)
        end=time.time()
        print(end-start)
        return result

    return wrapper

@timer
def square(nums):
    for i in nums:
        print(f'Square of {i} is {i*i}')

@timer
def cube(nums):
    for i in nums:
        print(f'Cube of {i} is {i*i*i}')

nums=[1,2,3,4]
square(nums)
cube(nums)




