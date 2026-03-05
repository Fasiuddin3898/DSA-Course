# right rotate an array by one place we can do this with two methods

# Method 1 slicing whose TC is O(N)

def slicing(nums):
    # if we store the value in nums[:] then it won't create a new adress for the nums it will store in same
    n=len(nums)
    nums[:]=[nums[-1]]+nums[0:n-1]
    print(f'nums in slicing {nums}')
    return nums

def for_loop(nums):
    n=len(nums)
    temp=nums[-1]
    for i in range(n-2,-1,-1):
        nums[i+1]=nums[i]

    nums[0]=temp
    print(f'nums in for loop {nums}')
    return nums


def main():
    nums=list(map(int,input().split(" ")))
    slicing(nums)
    for_loop(nums)

if __name__=="__main__":
    main()