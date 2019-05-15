#include <iostream>
#include <unordered_set>
#include <algorithm>
#include <vector>
#include <string>
#include <numeric>
#include <queue>
using namespace std;
const int dx[] = { 1, -1, 0, 0 };
const int dy[] = { 0, 0, 1, -1 };

class Solution {
	void dfs(int i, int j, vector<vector<char>> &board) {
		board[i][j] = 'A';
		for (int k = 0; k < 4; ++k) {
			int nx = i + dx[k], ny = j + dy[k];
			if (nx < 0 || ny < 0 || nx >= board.size() || ny >= board[0].size())
				continue;
			if (board[nx][ny] == 'O') {
				dfs(nx, ny, board);
			}
		}
	}

public:
	void solve(vector<vector<char>>& board) {
		if (board.empty()) return;
		for (int i = 0; i < board.size(); ++i) {
			if (board[i][0] == 'O')
				dfs(i, 0, board);
			if (board[i][board[0].size() - 1] == 'O')
				dfs(i, board[0].size() - 1, board);
		}
		for (int j = 0; j < board[0].size(); ++j) {
			if (board[0][j] == 'O')
				dfs(0, j, board);
			if (board[board.size() - 1][j] == 'O')
				dfs(board.size() - 1, j, board);
		}
		for (int i = 0; i < board.size(); ++i) {
			for (int j = 0; j < board[0].size(); ++j) {
				if (board[i][j] == 'A')
					board[i][j] = 'O';
				else if (board[i][j] == 'O')
					board[i][j] = 'X';
			}
		}
	}
};