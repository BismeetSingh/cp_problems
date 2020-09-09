#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
#https://leetcode.com/problems/number-of-islands/
class Solution:


    def dfs(self,grid,row,column):

        if row<0 or column<0 or row>len(grid)-1 or column>len(grid[0])-1:
            return

        if grid[row][column]=='0':
            return
        grid[row][column]='0'

        self.dfs(grid,row-1,column)
        self.dfs(grid,row+1,column)
        self.dfs(grid,row,column+1)
        self.dfs(grid,row,column-1)


    def numIslands(self, grid: List[List[str]]) -> int:
        count =0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]=='1':
                    self.dfs(grid,i,j)
                    count+=1
        return count
# @lc code=end

