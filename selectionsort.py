# look for the minimum number index in a array for selection sort 
#here time complexity will be n(n+1)/2 which will be 0(n*n) and space complexity is o(1)

def main():
    numbers = list(map(int,input().split(" ")))
    aced(numbers)
    decending(numbers)

def aced(numbers):
    for i in range(0,len(numbers)-1):
        min_index=i
        for j in range(i+1,len(numbers)):
            if numbers[j]<numbers[min_index]:
                min_index=j
        numbers[i],numbers[min_index]=numbers[min_index],numbers[i]
    print(numbers)

def decending(numbers):
    for i in range(0,len(numbers)-1):
        max_index=i
        for j in range(i+1,len(numbers)):
            if numbers[j]>numbers[max_index]:
                max_index=j
        numbers[i],numbers[max_index]=numbers[max_index],numbers[i]
    print(numbers)


if __name__=="__main__":
    main()