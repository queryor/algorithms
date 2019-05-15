'''Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'.
 Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. 
Two cells are connected if they are adjacent cells connected horizontally or vertically.'''

class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board: return
        m , n = len(board),len(board[0])
        vis =[[False for j in range(n)]for i in range(m)]
        dx,dy= [1,-1,0,0],[0,0,1,-1] ##四种移动方式
        for i in range(m):
            for j in range(n):
                if board[i][j]=='X' or vis[i][j]: continue
                q,q2=[],[]
                flag = True
                q.append((i,j))
                q2.append((i,j))
                while q:
                    curx ,cury=q.pop(0)
                    for k in range(4):
                        nx , ny = curx+dx[k],cury+dy[k]
                        if nx < 0 or ny <0 or nx >=m or ny>=n:
                            flag=False
                            continue
                        if vis[nx][ny] or board[nx][ny]=='X': continue
                        vis[nx][ny]= True
                        q.append((nx,ny))
                        q2.append((nx,ny))
                
                if flag:
                    for x,y in q2:
                        board[x][y]='X'
# 但其实有更简单的方法： 将边界上的点及其可达的O标记为‘A’，然后遍历board, 将A改为O, 将O改为X即可。
    def dfs(self, i, j, board):
        if board[i][j] != 'O': return
        board[i][j] = 'A'
        for nx, ny in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if nx < 0 or ny < 0 or nx >= len(board) or ny >= len(board[0]):
                continue
            self.dfs(nx, ny, board)
    
    def solve1(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]: return
        for i in range(len(board)):
            self.dfs(i, 0, board)
            self.dfs(i, len(board[0]) - 1, board)
        
        for j in range(len(board[0])):
            self.dfs(0, j, board)
            self.dfs(len(board) - 1, j, board)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'A':
                    board[i][j] = 'O'