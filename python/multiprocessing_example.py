# Multipleprocessing is multiple independent processes
# Each has seperate memory
# Runs on multple CPU cores(true partallelism)

# from multiprocessing import Process
# import time

# def compute():
#     total = 0
#     for i in range(10**7):
#         total += i

# processes = []
# start=time.time()

# for _ in range(2):
#     p = Process(target=compute)
#     p.start()
#     processes.append(p)

# for p in processes:
#     p.join()

# print(f'process completed in {time.time()-start}')

# Multiprocessing
# Video rendering
# AI/ML training
# Data processing pipelines

# When to use what (Golden Rule)
# Situation	            Use
# Waiting tasks	        Multithreading
# Heavy CPU work     	Multiprocessing

import time
import multiprocessing

square_result=[]

def square(nums):
    ans=[]
    global square_result
    for num in nums:
        ans.append(num*num)
        print(f'calculate the square {num*num}')
        square_result.append(num*num)
        time.sleep(0.1)
    print(f'Squares of a given array {ans}')
    print(f'print the square result for global variable inside the square function {square_result}')
    return ans

def cube(nums):
    ans=[]
    for num in nums:
        ans.append(num*num*num)
        print(f'calculate the cube {num*num*num}')
        time.sleep(0.1)
    print(f'Cubes of a given array {ans}')
    return ans

if __name__=="__main__":
    start=time.time()
    nums=[1,2,3,4]
    p1=multiprocessing.Process(target=square,args=(nums,))
    p2=multiprocessing.Process(target=cube,args=(nums,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(f'my task is ended now {time.time()-start}')  
    print(f'print the square result for global variable in main function {square_result}')

# If you open activity monitor we can see three python process because it uses seperate memory and multiple process which can not be seen in multithreading

# Lets to understand better lets store the result in global variable
# as we can see here we have 3 different processes square, cube and main we can not print the square_result in main process as that is getting appened in square process
# this can not be seen in multi threading as there we use the single process
# if we open the activity monitor we can see the four process one is for helper/system process(temporay) 
# Every process has its own address space(virtual memory). Thus program variables are not shared between two processes.You need to use interprocess communication(IPC) techniques if you want to share data between two processes


