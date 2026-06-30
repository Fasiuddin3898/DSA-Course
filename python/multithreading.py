# Lets calculate the square and cubes of a number parallely using threading
# If we use the below code it will first execute the square() function and then fter the cube() function

import time

def square(nums):
    ans=[]
    for num in nums:
        ans.append(num*num)
        print(f'calculate the square {num*num}')
        time.sleep(0.1)
    print(f'Squares of a given array {ans}')
    return ans

def cube(nums):
    ans=[]
    for num in nums:
        ans.append(num*num*num)
        print(f'calculate the cube {num*num*num}')
        time.sleep(0.1)
    print(f'Cubes of a given array {ans}')
    return ans
    
# nums=[1,3,5,7]
# t=time.time()
# square(nums)
# cube(nums)

# print(f'I completed the tasks in this time {time.time()-t}')


# Now if we use the multithreading and do this sum as this it will be like we create threads 
import threading
nums=[1,3,5,7] 
t=time.time()

T1=threading.Thread(target=square,args=(nums,)) #we try to run them parallely
T2=threading.Thread(target=cube,args=(nums,)) # args is tuple we can pass multiple arguments

T1.start()  #start the thread
T2.start()

T1.join() # Wait untils the T1 is done the thread which is started
T2.join() # Wait untils the T2 is done the thread which is started

print(f'I completed the tasks in this time {time.time()-t}')

# Defination: Multithreading is a thechnique that allows a single process to execute multiple threads concurrently.
# because the threds share the same memory space and resource, they can communicate ans share information more easily then seperate process
# GIL (Global Interpreter Lock) is a critical future in standard python, The Global Interpreter Lock ensures only one thread executes python bytecode at given moment
# Because of this, python multiple threading typically achives concurrency but not true parallelism(where tasks run at the exact same instant on different CPU cores)

#Solid example of multi threading is input/output Bound tasks

def download():
    print(f'start downloading')
    time.sleep(0.2)

download()
download()
download()

#Instead of above we do this
threads=[]
start=time.time()

for _ in range(3):
    tread=threading.Thread(target=download)
    tread.start()
    threads.append(tread)

for thread in threads:
    thread.join()

print(f' time taken to complete {time.time()-start}')

#Multithreading
# Web scraping (multiple URLs)
# Chat apps (handle many users)
# File downloads


# Difference between multithreading and multitasking
# Both are used to achieve multitasking
# Multiple threads leaves within in the same process 
# The benefit of multiprocessing is that error or memory leak in one process won't hurt execution of another process



