def main():
    lst=list(map(int,input().split(" ")))
    n=len(lst)
    for i in range(n-1):
        if lst[i]>lst[i+1]:
            print(f'array is not sorted')
            return
    print(f'array is sorted')
    return

if __name__=="__main__":
    main()