
# class Trie:
#     def __init__(self,node):
#         self.node=Tr
from collections import defaultdict
# class Trie:
#     def __init__(self,node):

class TrieNode:
    def __init__(self):
        self.chardict=defaultdict(list)

    def insert(self,word):
        current=self.chardict
        for c in word:
            if c not in current:
                current[c]=defaultdict(list)
            current=current[c]
        #End of word insertion character.
        current["#"]=1

    def search(self,word):
        current=self.chardict
        for c in word:
            #Check if current character exists in the parent's dictionary
            if c not in current:
                return False
            current=current[c]
        #if we reach the "#" then we found the matching word.
        return "#" in current

    def hasPrefix(self,word):
        current=self.chardict
        for c in word:
            #Check if current character exists in the parent's dictionary
            if c not in current:
                return False
            current=current[c]
        #partial matches should return true.
        return True

trie = TrieNode()
word="abc"
word4="aaa"
word1="bcd"
word2="ade"
trie.insert(word)
trie.insert(word1)
trie.insert(word4)
trie.insert(word2)
print(trie.search("aaaa"))
print(trie.hasPrefix("aa"))
# trie.print_dict()


    