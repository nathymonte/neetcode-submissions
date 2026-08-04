class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        squares = defaultdict(set)


        for r in range(9):
            for c in range(9):
                v = board[r][c]
                if v != ".":
                    if v in rows[r]:
                        return False
                    else:
                        rows[r].add(v)
                    if v in columns[c]:
                        return False
                    else:
                        columns[c].add(v)
                    s = (r // 3) * 3 + (c // 3)
                    if v in squares[s]:
                        return False
                    else:
                        squares[s].add(v)
        
        return True




        
        

            



            