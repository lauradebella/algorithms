#! /usr/bin/python

# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.


class Solution(object):
    
    def removeDuplicates(self, nums):
        i = 0
        print range(len(nums))
        for num in nums:
            if i != 0:
                if nums[i-1] == nums[i]:
                    while (nums[i-1] == nums[i] and i <len(nums)):
                        del nums[i]
                        if i == len(nums):
                            break
            i = i+1

        return len(nums)


solution = Solution()
print solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4])


