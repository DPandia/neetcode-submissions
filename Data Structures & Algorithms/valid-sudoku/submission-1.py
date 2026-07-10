class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        col = collections.defaultdict(set) # Creates dict with value as empty set
        row = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for i in range(9):
            for j in range(9):
                ele = board[i][j]
                if board[i][j]!='.':
                    if board[i][j] in row[i] or board[i][j] in col[j] or board[i][j] in squares[(i//3,j//3)]:
                        return False
                    else:
                        row[i].add(ele)
                        col[j].add(ele)
                        squares[(i//3,j//3)].add(ele)
        return True

                

