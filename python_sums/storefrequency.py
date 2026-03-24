def storefreq(given_list):
    result = {}

    for i in given_list:
        if i in result:
            result[i]+=1
        else:
            result[i]=1
    print(result)
    return result
def main():
    given_list = map(int,input().split(" "))
    storefreq(given_list)
if __name__ == "__main__":
    main()

