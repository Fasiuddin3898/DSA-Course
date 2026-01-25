s="xyxyxywywytytytyAWYHHHHDFGHRTYaaaaa" 
q=["x","y","w","A","a","H","M"]

hash_list=[0]*53

for char in s:
    asci_char=ord(char)
    index_value=asci_char-76
    hash_list[index_value]+=1

for char in q:
    asci_char=ord(char)
    index_value=asci_char-76
    print(f'{char} appeared {hash_list[index_value]} times in string {s}')