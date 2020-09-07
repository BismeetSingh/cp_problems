#use hashmaps
#make a deepcopy of the linked list.
#the idea is to make usual singly first ans then copy over the randoms from the hashmap.
#Question link : https://leetcode.com/problems/copy-list-with-random-pointer/
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        node=tmp=ListNode(0)
        curr=head
        i=0
        m={}
        while(curr):
            tmp.next=Node(curr.val)
            tmp=tmp.next
            m[curr]=tmp
            curr=curr.next
            i+=1
        curr=head
        
        while(curr):
            #Copy the reference of the random pointer to the corresponding node.
            if  curr.random:
                m[curr].random=m[curr.random]
            curr=curr.next
        
        return node.next
