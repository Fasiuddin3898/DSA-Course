# In insertion sort we compare the before element and traverse back the list

def insertion(lst):
    n=len(lst)
    for i in range(1,n):
        key=lst[i]
        j=i-1
        while j>=0 and lst[j]>key:
            lst[j+1]=lst[j]
            j-=1
        lst[j+1]=key
    return lst
def main():
    lst=list(map(int,input().split(" ")))
    print(f'sorted {insertion(lst)}')
    return insertion(lst)

if __name__=="__main__":
    main()

            

            

