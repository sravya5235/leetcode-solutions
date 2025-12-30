class Solution:
    def numMagicSquaresInside(self, grid):
        rows, cols = len(grid), len(grid[0])
        
        def isMagic(r, c):
            nums = set()
            
            # Collect numbers and validate range
            for i in range(3):
                for j in range(3):
                    val = grid[r + i][c + j]
                    if val < 1 or val > 9:
                        return False
                    nums.add(val)
            
            # Must be exactly 9 unique numbers
            if len(nums) != 9:
                return False
            
            # Check rows and columns
            for i in range(3):
                if sum(grid[r + i][c + j] for j in range(3)) != 15:
                    return False
                if sum(grid[r + j][c + i] for j in range(3)) != 15:
                    return False
            
            # Check diagonals
            if grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != 15:
                return False
            if grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != 15:
                return False
            
            return True
        
        count = 0
        for i in range(rows - 2):
            for j in range(cols - 2):
                if isMagic(i, j):
                    count += 1
        
        return count
