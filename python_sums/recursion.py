#when a function call itself is called recursion
# In tail recursion first function will be called and after the job will be done in head recursion first jobe will be done and then 
# function will call itself again
# print X, N times is question lets say print 2 15times


def req(x,n):
    if n==0:
        return
    req(x,n-1)
    print(f'printing the {x} for {n} time')

def req2(i,n):
    if i>n:
        return
    print(i)
    req2(i+1,n)

def main():
    # req(2,15)
    req2(1,5)

if __name__=="__main__":
    main()