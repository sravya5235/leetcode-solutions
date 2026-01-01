class Solution:
    def latestDayToCross(self, row: int, col: int, cells):
        parent = list(range(row*col + 2))
        rank = [0] * (row*col + 2)
        TOP, BOTTOM = row*col, row*col + 1
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return
            if rank[px] < rank[py]:
                parent[px] = py
            else:
                parent[py] = px
                if rank[px] == rank[py]:
                    rank[px] += 1
        
        grid = [[0]*col for _ in range(row)]
        
        def index(r, c):
            return r * col + c
        
        for day in range(len(cells)-1, -1, -1):
            r, c = cells[day]
            r -= 1
            c -= 1
            grid[r][c] = 1
            
            idx = index(r, c)
            if r == 0:
                union(idx, TOP)
            if r == row - 1:
                union(idx, BOTTOM)
            
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc]:
                    union(idx, index(nr, nc))
            
            if find(TOP) == find(BOTTOM):
                return day
