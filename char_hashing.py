s="xyxyxywywytytyty" 
q=["x","y","w"]

# #first method
# dit={}
# for i in s:
#     print(i)
#     dit[i]=dit.get(i,0)+1
# for char in q:
#     print(f'{char} came {dit.get(char)} times in {s}')

# 2nd method using the ascii works for only small charecters
hash_list=[0]*27
for char in s:
    asci_value=ord(char)
    index_value=asci_value-97
    hash_list[index_value]+=1
print(hash_list)

for char in q:
    index_value=ord(char)-97
    print(f'{char} appeared {hash_list[index_value]} times in {s} string')