#Question Link : https://leetcode.com/problems/all-elements-in-two-binary-search-trees/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    def inorder(self,root,ans):
        if root and root.left:
            # rootFlag=True
            self.inorder(root.left,ans)
        if root:
            ans.append(root.val)
            # print(root.val)
        if root and root.right:
            # rootFlag=True
            self.inorder(root.right,ans)
        return ans
        
    def merge(self,ans_root1,ans_root2):
        ans=[]
        l1=l2=0
        while(l1<len(ans_root1) and l2<len(ans_root2)):
            if ans_root1[l1]>=ans_root2[l2]:
                ans.append(ans_root2[l2])
                l2+=1
            else:
                ans.append(ans_root1[l1])
                l1+=1
        while l1<len(ans_root1):
            ans.append(ans_root1[l1])
            l1+=1
        while l2<len(ans_root2):
            ans.append(ans_root2[l2])
            l2+=1
        return ans
                

            
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        ans_root1=self.inorder(root1,[])
        ans_root2=self.inorder(root2,[])
        # print(ans_root1,ans_root2)
        return self.merge(ans_root1,ans_root2)
        