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
class Solution:
    
    def solve(self,root,s):
        if root:
            s+=str(root.val)
            self.solve(root.left,s)
            self.solve(root.right,s)
            if root.left is None and root.right is None:
                self.bt.append(s)

    #Searching in kmp algorithm. 
    #the basic idea is not to go fully backwards but find the point upto the last mismatch. 
    def kmp(self,src,dest,table):
        i=0
        j=0
        while(i<len(dest) and j<len(src)):
            if dest[i]==src[j]:
                i+=1
                j+=1
            else:
                if j!=0:
                    j=table[j-1]
                else:
                    i+=1
            if j==len(src):
                return True
        return False
                      
        
    def make_table(self,s):
        if len(s)==0:
            return []
        l=[0]*len(s)
        i=0
        j=1
        while(i<len(s) and j<len(s)):
            if s[i]!=s[j]:
                if i==0:
                    j+=1
                else:
                    i=l[i-1]
                    j+=1
            else:
                i+=1  
                l[j]=i
                j+=1
        return l
                    
    
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        
        if not head or not root:
            return False
        ll=[]
        self.bt=[]
        self.solve(root,"")
        print(self.bt) 
        while(head):
            ll.append(str(head.val))
            head=head.next
        ll="".join(ll)
        table=self.make_table(ll)
        for i in self.bt:
            if self.kmp(ll,i,table):
                return True
        return False
           
                
                
                
            
        