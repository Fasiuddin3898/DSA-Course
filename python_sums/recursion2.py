# sum of i to n parameters

def sum_num(sum,i,n):
    if i>n:
        print(sum)
        return
    sum_num(sum+i,i+1,n)

def main():
    # sum_num(0,2,9)
    # sum_num2(10)
    print(sum_num2(10))

# functional recurssion
def sum_num2(n):
    if n==1:
        return 1
    return n+sum_num2(n-1)


if __name__=="__main__":
    main()
