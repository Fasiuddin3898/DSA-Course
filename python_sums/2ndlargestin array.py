def main():
    ans()

def ans():
    n=list(map(int,input().split(" ")))
    n.sort()
    n_set=list(set(n))
    print(f'sorted list{n_set[1]}')

if __name__ == "__main__":
    main()