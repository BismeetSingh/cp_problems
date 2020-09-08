#
# @lc app=leetcode id=513 lang=python3
#
# [513] Find Bottom Left Tree Value
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:

        if not root:
            return -1
        q=[root]
        ans=0
        while q:
            tmp =[]
            while q:
                tmp.append(q.pop(0))
            if len(tmp)>0:
                child=tmp[0]
                isLast=False
                for nodes in tmp:
                    if nodes.left:
                        isLast=True
                        q.append(nodes.left)
                    if nodes.right:
                        isLast=True
                        q.append(nodes.right)
                if  not isLast:
                    return child.val
        
# @lc code=end

