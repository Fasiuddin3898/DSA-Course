
def main():
    number =int(input())
    factors(number)

def factors(number):
    result =[]
    for i in range(1,int(number**0.5)+1):
        if number%i==0:
            result.append(i)
            if i != number//i:
                result.append(number//i)
    result.sort()
    print(result)
    return result

if __name__ =="__main__":
    main()

