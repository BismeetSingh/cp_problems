#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        count=0
        while i<len(nums):
            j=i
            while j<len(nums) and nums[j]==val:
                j+=1
            if j<len(nums):
                count+=1
                nums[i],nums[j]=nums[j],nums[i]
            i+=1
        return count
        
# @lc code=end

