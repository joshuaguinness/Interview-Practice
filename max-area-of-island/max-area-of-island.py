class Solution:
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        # Start at grid space 0,0
        # Iterate through length then width
        # Everytime hit a 1, do dfs on that and change all the squares to something else
        # in that dfs, keep track of how many 1's there are
        # Keep track of a max of the max number of islands
        
        max_area = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    local_max = self.dfs(i, j, grid)
                    max_area = max(max_area, local_max)
        return max_area
                    
    def dfs(self, i, j, grid):
        
        if (i<0 or j<0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] == 0):
            return 0
        
        grid[i][j] = 0
        a = self.dfs(i+1,j, grid)
        b = self.dfs(i-1,j, grid)
        c = self.dfs(i,j+1, grid)
        d = self.dfs(i,j-1, grid)
        
        return (1 + a + b + c + d)