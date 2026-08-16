class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0
        
        def get_area(r, c):
            # 1. Out of bounds or water check
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0
            
            # 2. Mark as visited by turning it into 0
            grid[r][c] = 0
            
            # 3. Count self (1) + explore all 4 neighbors
            return (
                1 
                + get_area(r - 1, c)  # Up
                + get_area(r + 1, c)  # Down
                + get_area(r, c - 1)  # Left
                + get_area(r, c + 1)  # Right
            )

        # 4. The Scanner: loop through every cell in the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    current_area = get_area(r, c)
                    max_area = max(max_area, current_area)
                    
        return max_area