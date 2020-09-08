#
# @lc app=leetcode id=515 lang=python3
#
# [515] Find Largest Value in Each Tree Row
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        ans=[]
        q=[root]
        while q:
            tmp=[]
            m=float("-inf")
            while q:  
                tmp.append(q.pop(0))
                m=max(m,tmp[-1].val)
            if len(tmp)>0:
                ans.append(m)
                for child in tmp:
                    if child.left:
                        q.append(child.left)
                    if child.right:
                        q.append(child.right)
        return ans

        
# @lc code=end

