#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m=nums[0]
        currentMax=nums[0]
        for i in nums[1:]:
            currentMax=max(currentMax+i,i)
            # print(currentMax)
            m=max(m,currentMax)
        return m
        
# @lc code=end

