#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#

# @lc code=start
#Similar to no of islands problem
from collections import deque
class Solution:


    def bfs(self,matrix,queue,visited):
        directions=[[0,-1],[0,1],[1,0],[-1,0]]
        while queue:
            row,column=queue.popleft()
            for k in range(4):
                new_row=row+directions[k][0]
                new_column=column+directions[k][1]
                if new_row<len(matrix) and new_column<len(matrix[0]) and new_row>=0 and new_column>=0:
                    if matrix[new_row][new_column]>=matrix[row][column]:
                        if (new_row,new_column) not in visited:
                            queue.append((new_row,new_column))
                            visited.add((new_row,new_column))

    
#Question asked us to find path from cells to Water. Water can only flow from high to lower. The approach is to do the reverse for both the oceans.
#Instead of finding the path from cells to Water, we find the path from water to cells.
#So,we find lower to higher rather than higher to lower.
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        ans=[]
        #Pacific
        pacificSeen=set()
        pacificQueue=deque()
        
        for i in range(len(matrix)):
            pacificSeen.add((i,0))
            pacificQueue.append((i,0))

        for i in range (len(matrix[0])):
            pacificSeen.add((0,i))
            pacificQueue.append((0,i))

        #Atlantic
        atlanticSeen=set()
        atlanticQueue=deque()
        
        for i in range(len(matrix)):
            atlanticSeen.add((i,len(matrix[0])-1))
            atlanticQueue.append((i,len(matrix[0])-1))

        for i in range (len(matrix[0])-1):
            atlanticSeen.add((len(matrix)-1,i))
            atlanticQueue.append((len(matrix)-1,i))


        self.bfs(matrix,pacificQueue,pacificSeen)
        self.bfs(matrix,atlanticQueue,atlanticSeen)
        return [list(points) for points in atlanticSeen.intersection(pacificSeen)]
        # return [atlanticSeen.intersection(pacificSeen)]
# @lc code=end

