n=[5,3,2,2,1,5,5,7,15,10]
m=[10,111,1,9,5,67,2]
#count how many time m item present in n list
hash_list=[0]*16
print(hash_list)
for num in n:
    print(num)
    hash_list[num]+=1
for num in m:
    if num>16:
        print("num is not present")
    else:
        print(f'{num} came {hash_list[num]} times in {n}')