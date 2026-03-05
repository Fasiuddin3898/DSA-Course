# def outer(a):
#     print(f'value of a {a}')
#     def inner(b):
#         return a+b
#     return inner

# ans=outer(5)
# print(f'ans {ans}')
# print(f'ans10 {ans(10)}')

# def decorator(func):
#     def wrapper():
#         print(f'transaction statrted')
#         func()
#         print(f'transcation ended')
#     return wrapper

# def hello():
#     print(f'..Executing all steps on transaction..')

# hello1=decorator(hello)
# hello1()

# @decorator
# def hello2():
#     print(f'example execute all my transactions')

# hello2()

import time

# def timer(func):
#     def wrapper(*args):
#         start=time.time()
#         result=func(*args)
#         print("Time:",time.time()-start)
#         return result
#     return wrapper

# @timer
# def func_2():
#     print("hello")

# func_2()

def timer2(func):
    def wrapper(*args,**kargs):
        start=time.time()
        result=func(*args,**kargs)
        end=time.time()
        print(f'Executed {func.__name__} in {end-start:.4f}s')
        return result
    return wrapper

@timer2
def myfunc(a,b,c=12):
    print(f'sum of all the numbers {a+b+c}')

myfunc(1,2)

def timer3(func):
    def wrapper(*args):
        start=time.time()
        end=time.time()
        print(f'function has takend {end-start}s to execute the {func.__name__}')
        ans=func(*args)
        return None
    return wrapper

@timer3
def func4(a,b,c,d,e,f):
    print(f'multply all args {a*b*c*d*e*f}')
    return

func4(1,2,3,4,5,6)