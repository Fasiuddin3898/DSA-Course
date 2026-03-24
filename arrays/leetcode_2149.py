#Rearrange elements by signs
def rearrange(arr):
    n=len(arr)
    result=[0]*n
    positve=0
    negative=1
    for i in arr:
        if i>0:
            result[positve]=i
            positve+=2
        else:
            result[negative]=i
            negative+=2
    print(f'result {result}')
    return result

def main():
    lst=list(map(int,input().split(" ")))
    rearrange(lst)

if __name__=="__main__":
    main()