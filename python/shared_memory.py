# This is the example of how to share the memory between two processes as we know the processes creates their own virtual memory so the child process just initialize the copy of that varibale
# Using shared memory we can achieve this by shared array or shared value

# Shared array and shared value

import multiprocessing

def square(nums,result,v):
    ans=[]
    v.value=5.67
    for index,num in enumerate(nums):
        ans.append(num*num)
        result[index]=num*num
    print(f'result variable in square process {result[:]}')
    print(f'ans {ans}')
    return


if __name__=="__main__":
    nums=[1,2,3]
    result=multiprocessing.Array('i',3) # i means indeger d means double, 3 is the length of the array we defined
    v=multiprocessing.Value('d',0.9)
    process=multiprocessing.Process(target=square,args=(nums,result,v))
    process.start()
    process.join()
    print(f'print result in main process {result[:]}')
    print(f'print the value in main process {v.value}') # we defined value in main process and modified in child process still the value is taking from the child processes itself
