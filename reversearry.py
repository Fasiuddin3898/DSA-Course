# reverse only from 2 to 5 indexes from the array [1,2,3,4,5,6,7,8,9] -> for this replace left and right keys
def main():
    arr=[1,2,3,4,5,6,7,8,9]
    left=0
    right=len(arr)-1
    ans=rev(left,right,arr)
    print(ans)

def rev(left,right,arr):
    if left>=right:
        return arr
    arr[left],arr[right]=arr[right],arr[left]
    return rev(left+1,right-1,arr)

if __name__=="__main__":
    main()
