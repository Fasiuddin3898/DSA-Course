import multiprocessing 
import time

square_result=[]
square_result_example=[]
def square(nums):
    for i in nums:
        time.sleep(10)
        print(f'square {i**i}')
        square_result.append(i**i)
        square_result_example.append(i**i)
    print(f'square_result in this process {square_result}')


def cube(nums):
    for j in nums:
        time.sleep(10)
        print(f'cube {j**j**j}')



if __name__=="__main__":
    nums=[1,2,3,4,5]
    p1=multiprocessing.Process(target=square,args=(nums,))
    p2=multiprocessing.Process(target=cube,args=(nums,))
    p1.start()
    p2.start()

    p1.join()
    p2.join()


    print(f'square_result {square_result}')
    print(f'square_result_example {square_result_example}')
