# Tell the fibonic number at given input

def fibonic(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return fibonic(n-1)+fibonic(n-2)

def main():
    n=int(input())
    result=fibonic(n)
    print(result)

if __name__ =="__main__":
    main()

