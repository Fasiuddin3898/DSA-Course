import threading
import time

def square_number(arry):
    for i in arry:
        print(f'Square of a number {i**2}')

def cube_number(arry):
    for j in arry:
        print(f'cube of a number {j**3}')

arry=[1,2,3,4]

t1=threading.Thread(target=square_number,args=(arry,))
t2=threading.Thread(target=cube_number,args=(arry,))

t1.start()
t2.start()

t1.join()
t2.join()




