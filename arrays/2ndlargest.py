#Find the second largest element from the given array in most optimal way

def main():
    lst=list(map(int,input().split(" ")))
    frst_largest=float("-inf")
    scnd_largest=float("-inf")
    n=len(lst)
    for i in range(n):
        if lst[i]>frst_largest:
            scnd_largest=frst_largest
            frst_largest=lst[i]
        elif lst[i] > scnd_largest and lst[i] !=frst_largest:
            scnd_largest=lst[i]
    print(f'scnd_largest {scnd_largest}')
    return scnd_largest

if __name__=="__main__":
    main()