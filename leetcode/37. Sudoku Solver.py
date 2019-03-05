#https://leetcode.com/problems/sudoku-solver/
# Write a program to solve a Sudoku puzzle by filling the empty cells.

# A sudoku solution must satisfy all of the following rules:

# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# Empty cells are indicated by the character '.'.

# Note:

# The given board contain only digits 1-9 and the character '.'.
# You may assume that the given Sudoku puzzle will have a single unique solution.
# The given board size is always 9x9.
# 参考解法 http://www.cnblogs.com/grandyang/p/4421852.html
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if board == None or len(board)!=9 or len(board[0])!=9:
            return False
        self.solveSudokuDFS(board,0,0)


    def solveSudokuDFS(self,board,x,y):
        if x==9:
            return True
        if y>=9:
            return self.solveSudokuDFS(board,x+1,0)
        if board[x][y]=='.':
            for k in range(1,10):
                board[x][y]=str(k)
                if self.isValidSudoku(board):###这里其实没必要判断整个board是不是合法的，因为其他位置是合法的，只需要判断x,y位置是否合法就行了
                    if self.solveSudokuDFS(board,x,y+1):
                        return True
                board[x][y]='.'    
        else:
            return self.solveSudokuDFS(board,x,y+1)
        return False


    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
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
inputs = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
s.solveSudoku(inputs)
print(inputs)