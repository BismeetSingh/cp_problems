
# class Trie:
#     def __init__(self,node):
#         self.node=Tr
from collections import defaultdict
# class Trie:
#     def __init__(self,node):

class TrieNode:
    def __init__(self):
        self.root=defaultdict(list)
    

    def getIthbit(self,num,i):
        #Returns ith bit of the number.
        result =  num & (1<<i)
        if result ==0:
            return 0
        else:
            return 1
        
    def findMaximumXOR(self,nums):
        trie=TrieNode()
        for number in nums:
            current=self.root
            #from 31 to 1 because we care about the MSB bit first.
            for i in range(31,-1,-1):
                bit=self.getIthbit(number,i)
                #Xor the bits for 0-> or 1->0
                if bit^1 not in current:
                    current[bit^1]=defaultdict(list)
                current=current[bit^1]
        ans=float("-inf")
        for number in nums:
            current=self.root
            result=0
            for i in range(31,-1,-1):
                bit=self.getIthbit(number,i)
                if bit in current:
                    current=current[bit]
                    #if we get here means we either went 0->1 or went 1->0. In either this is a successful  1 placement at the MSB.
                    result+=(1<<i)
                else:
                    
                    current=current[bit^1]
            ans=max(ans,result)
        return ans



trie = TrieNode()
arr=[3,10,5,25,2,8]
print(trie.findMaximumXOR(arr))
