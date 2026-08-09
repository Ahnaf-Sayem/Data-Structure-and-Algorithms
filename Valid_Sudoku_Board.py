from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)
        for r in range(9):
            for c in range(9):
                 number = board[r][c]
                 if number == '.':
                    continue
                 else:
                       if number in rows[r] or number in cols[c] or number in squares[(r//3,c//3)]:
                           return  False
                       rows[r].add(number)
                       cols[c].add(number)
                       squares[(r//3,c//3)].add(number)
        return True
