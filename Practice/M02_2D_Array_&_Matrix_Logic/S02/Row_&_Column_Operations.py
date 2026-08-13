class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        col = len(grid[0])
        r = rows -1
        c = 0
        count = 0
        while r >= 0 and c <col:
            if grid[r][c] < 0:
                count += col - c
                r -= 1
            else:
                c += 1
        return count