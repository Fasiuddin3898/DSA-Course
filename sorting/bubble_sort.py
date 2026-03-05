


def bubblesort(lst):
    n=len(lst)

    for i in range(n-2,-1,-1):
        is_swaped=False  #for best case, to reduce the time complexity
        for j in range(i+1):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
                is_swaped=True
        if not is_swaped:  #we break the loop in one go only and TC will be O(n)
            break

    return lst

def main():
    lst=list(map(int,input().split(",")))
    print(bubblesort(lst))
    return bubblesort(lst)


if __name__=="__main__":
    main()

