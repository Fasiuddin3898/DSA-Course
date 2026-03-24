# palindrome using recursion

def palindrome(left,right,st):
    if left>=right:
        return 
    st[left],st[right]=st[right],st[left]
    return palindrome(left-1,right+1,st)

def palin(st):
    if st[::-1]==st:
        print(st[::-1])
        print(True)

def main():
    st="mom"
    palin(st)
    # left=0
    # right=len(st)-1
    # ans=palindrome(left,right,st)
    # if st==ans:
    #     print(True)

if __name__=="__main__":
    main()