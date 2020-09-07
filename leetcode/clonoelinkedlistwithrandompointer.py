#use hashmaps
#make a deepcopy of the linked list.
#the idea is to make usual singly first ans then copy over the randoms from the hashmap.
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
            
            if  curr.random:
                m[curr].random=m[curr.random]
            curr=curr.next
        
        return node.next