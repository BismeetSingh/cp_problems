#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#

# @lc code=start
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:

        if not matrix:
            return []
        
        ans=[[float("inf")]*len(matrix[0]) for j in range(len(matrix))]
        q=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==0:
                    q.append((i,j))
                    #Add all 0 cells to the queue.
                    ans[i][j]=0
                
        #Helps to lookup all the four directions.        
        directions=[[-1,0],[1,0],[0,-1],[0,1]]
        print(directions)
        while q:
            e=q.pop(0)
            x=e[0]
            y=e[1]
            for i in range(4):
                x1=x+directions[i][0]
                y1=y+directions[i][1]
                if x1>=0 and y1>=0 and (x1<len(matrix)) and (y1<len(matrix[0])):
                    if ans[x1][y1]>(ans[x][y]+1):
                        ans[x1][y1]=(ans[x][y]+1)
                        #We add cell to queue if we get a lower value because we need to update its neighbours again to reflect the lower value.
                        q.append((x1,y1))
        return ans
            



# @lc code=end

