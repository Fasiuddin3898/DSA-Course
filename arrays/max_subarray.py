def maxSubArray_brute(nums):  # Here TC is O(N)
    n=len(nums)
    max_sum=float("-inf")
    for i in range(n):
        j=i
        curr_sum=0
        while j<n:
            curr_sum=curr_sum+nums[j]
            max_sum=max(max_sum,curr_sum)
            j+=1
    return max_sum

def maxSubArray(nums):     # Optimal way also know as kadane's algorithm here TC is O(N) and SC is O(1)
    n=len(nums)
    max_sum=float('-inf')
    curr_sum=0
    for i in range(n):
        curr_sum+=nums[i]
        max_sum=max(curr_sum,max_sum)
        if curr_sum<0:
            curr_sum=0
    return max_sum

def main():
    nums=list(map(int,input().split(" ")))
    maxSubArray_brute(nums)
    maxSubArray(nums)

if __name__=="__main__":
    main()
