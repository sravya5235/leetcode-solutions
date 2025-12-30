class Solution:
    def numMagicSquaresInside(self, grid):
        rows, cols = len(grid), len(grid[0])
        
        def isMagic(r, c):
            if grid[r+1][c+1] != 5:
                return False
            
            nums = set()
            for i in range(3):
                for j in range(3):
                    nums.add(grid[r+i][c+j])
            
            if nums != set(range(1, 10)):
                return False
            
            s = 15
            return (
                grid[r][c] + grid[r][c+1] + grid[r][c+2] == s and
                grid[r+1][c] + grid[r+1][c+1] + grid[r+1][c+2] == s and
                grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2] == s and
                grid[r][c] + grid[r+1][c] + grid[r+2][c] == s and
                grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1] == s and
                grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2] == s and
                grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] == s and
                grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] == s
            )
        
        ans = 0
        for i in range(rows - 2):
            for j in range(cols - 2):
                if isMagic(i, j):
                    ans += 1
        
        return ans
