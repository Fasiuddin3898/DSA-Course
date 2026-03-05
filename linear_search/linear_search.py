# Do a linear search on the list and return the index if not found -1, if duplicate return -1

def linear(nums,k):
    n=len(nums)
    for i,num in enumerate(nums):
        if num==k:
            print(f'element found at index {i}')
            return i
        
    return -1

def main():
    nums=list(map(int,input().split(" ")))
    k=int(input())
    linear(nums,k)

if __name__=="__main__":
    main()