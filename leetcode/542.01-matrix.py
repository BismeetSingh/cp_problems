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

        ans =[[float("inf")]*(len(matrix[0])) for i in range(len(matrix))]
        # print(ans[0][0])

        q=[]
        # visited={}
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==0:
                    q.append((i,j))
                    ans[i][j]=0
                    

        r=len(matrix)
        c=len(matrix[0])
        
        
        while q:
            curr=q.pop(0)
            x=curr[0]
            y=curr[1]
            
            #Check bounds
            
            if y+1<c:


                if ans[x][y+1]>ans[x][y]+1:
                    ans[x][y+1]=ans[x][y]+1
                    q.append((x,y+1))




            if y-1>=0:
                if ans[x][y-1]>ans[x][y]+1:
                    ans[x][y-1]=ans[x][y]+1
                    q.append((x,y-1))
        

            if x+1<r:
                if ans[x+1][y]>ans[x][y]+1:
                    ans[x+1][y]=ans[x][y]+1
                    q.append((x+1,y))
               
                    

            if x-1>=0:
                if ans[x-1][y]>ans[x][y]+1:
                    ans[x-1][y]=ans[x][y]+1
                    q.append((x-1,y))
                

        return ans




# @lc code=end

