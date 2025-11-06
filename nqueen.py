class Solution:
    def solveNQueens(self, n):
        col = set()
        posDiag = set()
        negDiag = set()
        res = []
        board = [["."] * n for _ in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                # Stop after finding 8 solutions
                if len(res) == 8:
                    return True
                return False

            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                board[r][c] = "Q"
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)

                if backtrack(r + 1):
                    return True  # Stop early once 8 found

                board[r][c] = "."
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)

            return False

        backtrack(0)
        return res


# Run it
sol = Solution()
ans = sol.solveNQueens(8)
print("Showing 8 unique-looking solutions:")
for i, board in enumerate(ans, 1):
    print(f"\nSolution {i}:")
    for row in board:
        print(row)
