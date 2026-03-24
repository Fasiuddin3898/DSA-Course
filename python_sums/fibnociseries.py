#return fibnoci series from 0,1,1,2,3,5

def fibonic(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return fibonic(n-1)+fibonic(n-2)

def main():
    n=int(input())
    for i in range(1,n+1):
        ans=fibonic(i)
        print(ans,end=" ")

if __name__=="__main__":
    main()
