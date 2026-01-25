def rev(n,arr,new):
    if n<0:
        return new
    new.append(arr[n])
    return rev(n-1,arr,new)

def main():
    arr=[1,2,3,4,5,6]
    result = rev(len(arr)-1,arr,[])
    print(result)

if __name__=="__main__":
    main()
