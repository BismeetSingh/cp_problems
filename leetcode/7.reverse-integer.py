#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        i=10
        num=x
        ans=0
        x=abs(x)
        while x>0:
            rem=x%10
            ans=(ans*i)+rem
            x=x//10
        if num<0:
            ans=-ans
        if ans>(2**31)-1:
            return 0
        if ans<(-2**31)-1:
            return 0
        return ans
        
# @lc code=end

