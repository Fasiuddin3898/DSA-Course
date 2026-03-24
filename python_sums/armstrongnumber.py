import math
n=input()
len_ln=len(n)
num=int(n)
sum=0
while num>0:
    last_digit=num%10
    sum+=last_digit ** len_ln
    num=num//10
if sum == int(n):
    print(f'{n} is an armstrong number')
else:
    print(f'{n} is not an armstrong number')