# Sum of two elements whose sum is closest to the target, which means the difference should be closest 

def min_sum():
    lst=[1,4,6,8,10]
    n=len(lst)
    target=13
    max_number =float("inf")
    ans=()
    i=0
    j=n-1
    while i<j:
        sum_pair=lst[i]+lst[j]
        diff=abs(target-sum_pair)
        if diff<max_number:
            ans=(lst[i],lst[j])
            max_number=diff
        if sum_pair==target:
            break
        if sum_pair>target:
            j-=1
        else:
            i+=1

    print(f'ans {ans}')
    return

min_sum()
        




            




