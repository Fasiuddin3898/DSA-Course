# We repeatedly compare two adjacent elements in a list.
# If they are in the wrong order, we swap them.
# After one full pass, the largest element “bubbles up” to the end.
# We repeat these passes on the remaining unsorted part.
# The process stops when no swaps are needed, meaning the list is sorted.
#in bubble sort always remember we bring the largest element in end in every swap

def bubbleSort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        swapped = False

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if (swapped == False):
            break

def main():
    numbers=list(map(int,input().split(" ")))
    bubbleSort(numbers)

if __name__=="__main__":
    main()
