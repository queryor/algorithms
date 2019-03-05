# https://leetcode.com/problems/valid-sudoku/

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        #创建一个字典来判断是不是重复。 
        #更快的方法应该直接用一个数组。因为数字可以直接当索引，查找速度为O(1)
        grid = [{} for i in range(9)]
        for i in range(9):
            row = {}
            col = {}
            for j in range(9):
                if board[i][j] != '.' and board[i][j] not in row:
                    row[board[i][j]]=1
                elif board[i][j] in row:
                    return False
                if board[j][i] !='.' and board[j][i] not in col:
                    col[board[j][i]]=1
                elif board[j][i] in col:
                    return False
                grid_num = 3*(i//3) + j//3 #得到第几个格子
                if board[i][j]!='.' and board[i][j] not in grid[grid_num]:
                    grid[grid_num][board[i][j]]=1
                elif board[i][j] in grid[grid_num]:
                    return False
        
        return True

s = Solution()
inputs = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
# inputs = [
#   ["5","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]
print(s.isValidSudoku(inputs))