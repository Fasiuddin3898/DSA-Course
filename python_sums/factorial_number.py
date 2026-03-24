def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

def main():
    x=fact(4)
    print(x)

if __name__=="__main__":
    main()