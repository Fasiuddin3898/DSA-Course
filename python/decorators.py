# Decorators solve both the issues i.e
# 1.Code Duplication
# 2.Cluttering main logic of function with additional functionality(i.e timing in our logic)

# In the below example we are measuring the time taken by an function in milli seconds to execute using the wrapper and decorators

# Wrapper function defination : Functions are first class objects in python. What it means is that they can be treated just like any other variable
# and you can pass them as argument to another function or even return them as a return value
# Decorators act as a wrapper for your original function
# Common use cases of decorators Logging and Timing


import time

def timer(func):
    def wrapper(*a,**k):
        start=time.time()
        reuslt=func(*a,**k)
        end=time.time()
        print(f'function {func.__name__} has taken {(end-start)*1000} milli seconds')
        return reuslt
    return wrapper

@timer
def cube(nums):
    result=[]
    for num in nums:
        result.append(num*num*num)
    return result

if __name__=="__main__":
    nums=range(1,100000)
    cube(nums)


