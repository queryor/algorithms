# Given a 2D board and a word, find if the word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

# Example:

# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]

# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.

class Solution:
    def exist(self, board, word: str) -> bool:
        ### 直接搜索...
        if len(word)==0:
            return True
        m = len(board)
        if m==0:
            return False
        n = len(board[0])
        if n==0:
            return False
        for i in range(m):
            for j in range(n):
                if(self.serach(board,word,0,i,j)):
                    return True
        return False

    def serach(self,board,word,idx,i,j):
        if idx == len(word):
            return True
        m,n = len(board),len(board[0])
        if i<0 or j<0 or i>=m or j>=n or board[i][j]!=word[idx]:
            return False
        c = board[i][j]
        board[i][j]='#'
        res = self.serach(board,word,idx+1,i-1,j) or self.serach(board,word,idx+1,i,j-1) or \
        self.serach(board,word,idx+1,i+1,j) or self.serach(board,word,idx+1,i,j+1)
        board[i][j]=c
        return res
