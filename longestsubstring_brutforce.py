class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)

        lst=[]
        lst_unique=[]

        for i in range(0,n):
            for j in range(i+1,n+1):
                lst.append(s[i:j])

        for i in lst:
            sub_string=i
            dit={}
            for j in sub_string:
                dit[j]=dit.get(j,0)+1

            if all(value == 1 for value in dit.values()):
                lst_unique.append(sub_string)

        dit_1={}

        for string in lst_unique:
            dit_1[string]=len(string)
        max_value=0

        # print(dit_1)
        max_key=""
        for key,value in dit_1.items():
            if value>max_value:
                max_key=key
                max_value=value

        return max_value