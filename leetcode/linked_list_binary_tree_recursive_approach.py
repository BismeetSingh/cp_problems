# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#The idea is to start at every node with the same head. When we match a value we explore its right and left subtree.
class Solution:
    
    def dfs(self,root,head):
        
        if  root is None:
            return False
        if self.match(root,head):
            return True
            
        return self.dfs(root.left,head) or self.dfs(root.right,head)
        
        
    def match(self,root,head):
        if head is None:
            return True
        if root is None or root.val!=head.val:
            return False
        #Search for left and right subtree
        return self.match(root.left,head.next) or self.match(root.right,head.next)
        
                    
    
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        
        return self.dfs(root,head)
           
                
                
                
            
        