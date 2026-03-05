# Right rotate an array by k places

def brute(nums,k):
    n=len(nums)
    k=k%n
    for _ in range(k):  # TC for this is O(k)
        e=nums.pop()
        nums.insert(0,e)   #Time complexity for this is O(N)
    print(f'print answer in brute {nums}')    # Total TC is O(N*K)
    return nums

def better(nums,k):
    n=len(nums)
    k=k%n
    nums[:]=nums[n-k:]+nums[:n-k] # TC is O(N)
    print(f'print answer in better {nums}')
    return nums

def optimal(nums,k):
    n=len(nums)
    k=k%n
    reverse(nums,n-k,n-1)
    reverse(nums,0,n-k-1)
    reverse(nums,0,n-1)
    print(f'answer in optimal way {nums}')
    return nums

     

def reverse(nums,left,right):
    while left<right:
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1


def main():
    array=list(map(int,input().split(" ")))
    k=int(input())
    optimal(array,k)
    brute(array,k)

if __name__=="__main__":
    main()
