def substring(s):
    n=len(s)
    left=0
    right=0
    my_dict={}
    ans=""
    maxi=0
    while right<n:
        if s[right] in my_dict:
            left=max(left,my_dict[s[right]]+1)
        my_dict[s[right]]=right
        if right-left+1 > maxi:
            ans=s[left:right+1]
        maxi=max(maxi,right-left+1)
        right+=1
    print(f'maxi {maxi}')
    print(f'ans {ans}')
    return maxi
        
def main():
    s=input()
    ans=substring(s)

if __name__=="__main__":
    main()
