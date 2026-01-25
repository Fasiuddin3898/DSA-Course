n=input()
sum=0
num = int(n)
while num>0:
    last_digit = num%10
    sum = sum*10 +last_digit
    num=num//10
print(sum)
if sum==int(n):
    print('true')