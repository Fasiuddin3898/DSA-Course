def brute(nums):
    n=len(nums)
    max_sequence=0
    max_lst_seq=[]
    for i in range(n):
        count=0
        lst_seq=[]
        number=nums[i]
        while number in nums:
            count+=1
            number+=1
            lst_seq.append(number)
        if count>max_sequence:
            max_lst_seq=lst_seq
        max_sequence=max(max_sequence,count)
    print(f'max_sequence in brute {max_sequence} max_lst_seq {max_lst_seq}')
    return max_sequence

def better(nums):
    n=len(nums)
    nums.sort()
    last_smallest=float("-inf")
    max_sequence=0
    count=0
    for i in range(0,n):
        num=nums[i]

        if num-1==last_smallest:
            count+=1
            last_smallest=num
        elif num-1 != last_smallest:
            count=1
            last_smallest=num

        max_sequence=max(max_sequence,count)
    print(f'max_sequence in better {max_sequence}')
    return max_sequence

def optimal(nums):
    n=len(nums)
    my_set=set()
    for i in nums:
        my_set.add(i)
    max_sequence=0
    for num in my_set:
        if num-1 not in my_set:
            count=0
            x=num
            while x in my_set:
                count+=1
                x+=1

            max_sequence=max(max_sequence,count)

    print(f'max_sequence in optimal {max_sequence}')
    return max_sequence


def main():
    nums=[1 ,99 ,101 ,98 ,2 ,5, 3, 100, 1 ,1]
    brute(nums)
    better(nums)
    optimal(nums)

if __name__=="__main__":
    main()