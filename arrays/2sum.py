def twoSum_brute(nums, target):
    n=len(nums)
    for i in range(0,n-1):
        for j in range(i+1,n):
            if nums[i]+nums[j]==target:
                print(f'result {[i,j]}')
                return [i,j]
            
def main():
    lst=list(map(int,input().split(" ")))
    target=int(input())
    # twoSum_brute(lst,target)
    twoSum(lst,target)

def twoSum(nums,target):
    n=len(nums)
    hash_map={}
    for i in range(n): #TC is O(N)
        rem=target-nums[i]
        if rem in hash_map:    # TC to check the item in hash map is O(1)
            print(f' ans in optimal {[hash_map[rem],i]}')
            return [hash_map[rem],i]
        hash_map[nums[i]]=i

if __name__=="__main__":
    main()