# This problem is related to get the max profit when we sell the stock at given time
# So we try to get the min_number and store them in one varibale and subtract the current price with that store min_price


def main():
    lst=[7,2,1,5,6,4,8]
    min_price=float("inf")
    max_profit=float("-inf")
    n=len(lst)
    for i in range(n):
        min_price=min(lst[i],min_price)
        max_profit=max(max_profit,lst[i]-min_price)
    print(f'max_profit is {max_profit}')
    return max_profit

if __name__=="__main__":
    main()

