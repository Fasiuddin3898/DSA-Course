def main():
    lst=[1,8,6,2,5,4,8,3,7]
    n=len(lst)
    right=n-1
    left=0
    max_area=0
    while left<right:
        length=min(lst[left],lst[right])
        breadth=right-left
        area=length*breadth
        max_area=max(max_area,area)
        if lst[left]>lst[right]:
            right-=1
        else:
            left+=1
    print(f'maximum area of the container is {max_area}')



main()



