#
# @lc app=leetcode id=508 lang=python3
#
# [508] Most Frequent Subtree Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import Counter
class Solution:

    def solve(self,root):
        if root and not root.left and not root.right:
            self.m[root.val]+=1
            return root.val
        if not root:
            return 0
        if root:
            sum=0
            if root.left and root.right:
                sum=root.val+self.solve(root.left)+self.solve(root.right)
            elif root.right:
                sum=root.val+self.solve(root.right)
            elif root.left:
                sum=root.val+self.solve(root.left)
            # print(sum)
            self.m[sum]+=1
            return sum

    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        
        if not root or root.val == None:
            return []
        self.m=Counter()
        self.solve(root)
        # print(self.m)
        f=max(self.m.values())
        print(f)
        ans=[]
        for k,v in self.m.items():
            if v==f:
                ans.append(k)
        return ans
# @lc code=end

