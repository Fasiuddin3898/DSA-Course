# Remove duplicates from sorted array
# Leet code 26 Remove Duplicates from Sorted Array
# Given an integer array nums sorted in non-decreasing order, 
# remove the duplicates in-place such that each unique element appears only once. 
# The relative order of the elements should be kept the same.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return 1
        i=0
        j=i+1
        while j<n:
            if nums[j] != nums[i]:
                i+=1
                nums[i],nums[j]=nums[j],nums[i]
            j+=1
        return i+1

        