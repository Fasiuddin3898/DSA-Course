# Move zeros to end in an array
def main():
    lst=[0,1,8,6,0,2,5,4,8,0,3,7]
    n=len(lst)
    if n==1:
        return lst
    i=0
    while i<n:
        if lst[i]==0:
            break
        i+=1
    if i==n-1:
        print(f'sorted list if no zeros {lst}')
        return lst
    j=i+1
    while j<n:
        if lst[j] !=0:
            lst[i],lst[j]=lst[j],lst[i]
            i+=1
            j+=1

    print(f'sorted lst{lst}')

    return lst





main()
