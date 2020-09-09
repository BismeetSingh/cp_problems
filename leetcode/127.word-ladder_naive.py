#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#
#https://leetcode.com/problems/word-ladder/
#This is the most naive  approach
# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
          
        wordList=set(wordList)
        if endWord not in wordList:
            return 0
        queue=[beginWord]
        level=1
        s="abcdefghijklmnopqrstuvwxyz"
        while queue:
            size=len(queue)
            for i in range(size):
                #Pop the current word
                current_word=queue.pop(0)
                l=list(current_word)
                for i in range(len(l)):
                    ch=l[i]
                    #Try changing each character.
                    for character in s:
                        if l[i]==character:
                            continue
                        l[i]=character
                        newStr="".join(l)
                        if newStr==endWord:
                            return level+1
                        if  newStr in wordList:
                            queue.append(newStr)
                            wordList.remove(newStr)
                    l[i]=ch
            level+=1
        return 0
# @lc code=end

