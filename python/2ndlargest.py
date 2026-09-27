def main():
    lst=[55,32,97,-55,45,32,88,21,97,88,100,32,100]
    largest=float("-inf")
    largest_nd=float("-inf")
    for i in lst:
        if i>largest:
            largest_nd=largest
            largest=i
        elif i>largest_nd and i != largest:
            largest_nd=i

    print(f'largest_nd {largest_nd}')
    print(f'largest{largest}')

main()



