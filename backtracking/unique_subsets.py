# 78. Subsets
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given an integer array nums of unique elements, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

def main():
    nums=list(map(int,input().split(",")))
    print(f'nums {nums}')
    result=[]
    subset=[]
    def backtracking(index):
        if index >= len(nums):
            result.append(subset.copy())
            return
        #decide to include the index
        subset.append(nums[index])
        backtracking(index+1)

        #decide to exclude the index
        subset.pop()
        backtracking(index+1)

    backtracking(0)
    print(f'result {result}')
    return result

if __name__=="__main__":
    main()