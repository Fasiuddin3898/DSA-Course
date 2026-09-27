# Rotate the given array k times so what we do is first we get the moduleos of k
# 1. reverse last k elements 
# 2. reverse first k elements
# 3. reverse the whole array

def reverse(lst,left,right):
    while left<right:
        lst[left],lst[right]=lst[right],lst[left]
        left+=1
        right-=1
    return 

def rotate():
    lst=[1,2,3,4,5,6]
    n=len(lst)
    k=2
    rotation=k%n
    reverse(lst,n-rotation,n-1)
    reverse(lst,0,n-rotation-1)
    reverse(lst,0,n-1)
    print(f'lst after k rotations {lst}')
    return lst

rotate()
    