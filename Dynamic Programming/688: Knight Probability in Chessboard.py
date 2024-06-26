# https://leetcode.com/problems/knight-probability-in-chessboard/description/
# difficulty: medium
# topics: dynamic programming

# problem:
# On an n x n chessboard, a knight starts at the cell (row, column) and attempts to make exactly k moves. The rows and columns are 0-indexed, so the top-left cell is (0, 0), and the bottom-right cell is (n - 1, n - 1).
# A chess knight has eight possible moves it can make, as illustrated below. Each move is two cells in a cardinal direction, then one cell in an orthogonal direction.

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        cache = {}
        moves = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2)]

        def boardMoves(currRow, currCol):
            positions = []
            for (rowChange, colChange) in moves:
                newRow, newCol = currRow + rowChange, currCol + colChange
                if newRow >= 0 and newRow < n and newCol >= 0 and newCol < n:
                    positions.append((newRow, newCol))
            return positions

        def dp(currRow, currCol, remaining):
            if remaining == 0: return 1
            key = (currRow, currCol, remaining)
            if key in cache: return cache[key]
            positions = boardMoves(currRow, currCol)
            ans = 0
            for pos in positions:
                ans += dp(pos[0], pos[1], remaining-1) / 8
            cache[key] = ans
            return ans
        
        return dp(row, column, k)
# top-down with memoization
# time complexity: O(n*n*k)
# space complexity: O(n*n*k)
#     each states takes O(8) time
#     there are n*n*k states
