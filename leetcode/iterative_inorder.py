# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#Use a stack
#Go to leftmost child

class Solution:

    
    def inorderTraversal(self, root: TreeNode) -> List[int]:
         
        if not root:
            return []
        l=[]
        stack=[root]
        while True:
            while root and  root.left:
                stack.append(root.left)
                root=root.left
            if  len(stack)==0:
                break     
            top=stack.pop()
            l.append(top.val)
            root=top.right
            if root:
                #Add the right of t popped node.
                stack.append(root)

        return l
            
            
            
            
        