# Longest sequence in a list

def brute(nums):
    maxi=0
    n=len(nums)
    for i in nums:
        count=0
        number=i
        while number in nums:
            count+=1
            number+=1
        maxi=max(maxi,count)

    print(f'Longest sequence in a list {maxi}')
    return maxi

def better(nums):
    n=len(nums)
    nums.sort()   # Time complexity is O(N*LogN)
    last_smallest=float("-inf")
    count=0
    longest=0
    for num in nums:     #Time complexity is O(N)
        if num==last_smallest:
            continue
        elif num-1==last_smallest:
            count+=1
            last_smallest=num
        else:
            count=1
            last_smallest=num
        longest=max(longest,count)

    print(f' longest in better {longest}')
    return longest

def optimal(nums):   #Time complexity to search for any element is O(1) in set
    my_set=set()
    for i in nums:
        my_set.add(i)
    longest=0
    for i in my_set:
        if i-1 in my_set:
            continue
        else:
            num=i
            count=0
            while num in my_set:
                count+=1
                num+=1
            longest=max(longest,count)
    print(f'Longest in optimal {longest}')
    return longest

def main():
    lst=list(map(int,input().split(" ")))
    brute(lst)
    better(lst)
    optimal(lst)

if __name__=="__main__":
    main()
