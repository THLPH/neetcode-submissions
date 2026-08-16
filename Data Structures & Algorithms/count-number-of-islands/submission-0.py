class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        
        def counter(r, c):
            # 1. Out of bounds or water check
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0":
                return
            
            # 2. Mark as visited by turning it into 0
            grid[r][c] = "0"
            
            # 3. Explore all 4 neighbors
            
            counter(r - 1, c)  # Up
            counter(r + 1, c)  # Down
            counter(r, c - 1)  # Left
            counter(r, c + 1)  # Right
            

        # 4. The Scanner: loop through every cell in the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1
                    counter(r,c)
                    
        return count