#https://leetcode.com/problems/k-th-symbol-in-grammar/
#Break down the problem into subproblems
#N-1 , k because the elements before mid are same in previous row as in current row
#complement K-mid because after mid point the elements are inverted.
#(2**(N-1))//2 gives the no of elements in the nth row.
class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        
        if N==1 and K==1:
            return 0
        mid=(2**(N-1))//2
        if K<=mid:
            return self.kthGrammar(N-1,K)
        else:
            return  1^self.kthGrammar(N-1,K-mid)
        