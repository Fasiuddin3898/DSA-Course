# Always remember merge sort means divide and conqure which is divide and merge basically
# Here time complexity is O(N*LogN) as we are continously diving the array that is logN and mergeing is N
# Here space complexity is O(N)
# Most imported for intervies
def merge_sort(array):
    if len(array) <=1:
        return array
    mid=len(array)//2
    left_array=array[:mid]
    right_array=array[mid:]

    left=merge_sort(left_array)
    right=merge_sort(right_array)
    return merge_array(left,right)

def merge_array(left,right):
    result=[]
    i,j=0,0
    n,m=len(left),len(right)

    while i<n and j<m:
        if left[i] <=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

    if i<n:
        while i<n:
            result.append(left[i])
            i+=1
    if j<m:
        while j<m:
            result.append(right[j])
            j+=1

    return result

def main():
    lst=list(map(int,input().split(" ")))
    print(f'sorted array {merge_sort(lst)}')
    return

if __name__=="__main__":
    main()