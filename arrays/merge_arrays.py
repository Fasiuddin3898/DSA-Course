# Merge two sorted arrays without duplicates in it

# Example a1=[1,1,2,3,4,5,5] a2=[1,5,6,7,8] ans=[1,2,3,4,5,6,7,8]
# Example a1=[1,1,1,1,1] a2=[2,2,2,2] ans=[1,2]

# here TC is O(N+M) and SC is O(M+N) in worst case

def merge(nums1,nums2):
    n=len(nums1)
    m=len(nums2)
    result=[]
    i,j=0,0

    while i<n and j <m:
        if nums1[i] <nums2[j]:
            if len(result)==0 or result[-1]!=nums1[i]:
                result.append(nums1[i])

            i+=1
        else:
            if len(result)==0 or result[-1]!=nums2[j]:
                result.append(nums2[j])

            j+=1

    if i<n:
        while i<n:
            if len(result)==0 or result[-1]!=nums1[i]:
                result.append(nums1[i])

                i+=1
    if j<m:
        while j<m:
            if len(result)==0 or result[-1]!=nums2[j]:
                result.append(nums2[j])
            j+=1

    print(f'result {result}')
    return result

def main():
    nums1=list(map(int,input().split(" ")))
    nums2=list(map(int,input().split(" ")))
    merge(nums1,nums2)


if __name__=="__main__":
    main()

