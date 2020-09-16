
# class Trie:
#     def __init__(self,node):
#         self.node=Tr
from collections import defaultdict
# class Trie:
#     def __init__(self,node):

class TrieNode:
    def __init__(self):
        self.chardict=defaultdict(list)
        self.maximum=0

    def insert(self,word):
        #Simple trie insertion.
        current=self.chardict
        for c in word:
            if c not in current:
                current[c]=defaultdict(list)
            current=current[c]
        #End of word insertion character.
        current["#"]=1

    def search(self,word):
        current=self.chardict
        s=""
        for c in word:
            #if we get a 0,we want a 1 because 0 XOR 1 would bring us close to 1. We want 1 in the most significant bits
            #so as to get the largest possible number.
            if c=="0":
                toSearch="0"
                complement="1"
            elif c=="1":
                toSearch="1"
                complement="0"
            # 
            if complement in current:
                s+=complement
                current=current[complement]
            elif toSearch in current:
                # print("To Search",toSearch)
                s+=toSearch
                current=current[toSearch]
        print(s)
        a=int(word,2)
        b=int(s,2)
        #We take a maximum of the current xor number and the number we passed in the function.
        self.maximum=max(self.maximum,a^b)
            # print(current)
            # for k,v in current.items():
            #     print(k,v)
        #if we reach the "#" then we found the matching word.
        return "#" in current

    

trie = TrieNode()
arr=[3,10,5,25,2,8]
bits=[]
#We find binary  representation of each number and build a trie out of it.
for i in arr:
    binary=str(bin(i))
    binary=binary.replace("0b","")
    while len(binary)<32:
        binary="0"+binary
    bits.append(binary)

# print(bits)
#Insert in trie.
for i in bits:
    trie.insert(i)
#Search all binary nums in trie.
for i in bits:
    trie.search(i)

print(trie.maximum)
    