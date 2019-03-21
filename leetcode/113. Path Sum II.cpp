#include <iostream>
#include <unordered_set>
#include <algorithm>
#include <vector>
#include <string>
#include <numeric>
#include <queue>
using namespace std;



// Definition for a binary tree node.
 struct TreeNode {
     int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

 class Solution {
 public:
	 vector<vector<int>> pathSum(TreeNode* root, int sum) {
		 vector<vector<int>> res;
		 vector<int> out;
		 help(root, sum, out, res);
		 return res;
	 }
	 void help(TreeNode* node, int sum, vector<int>& out, vector<vector<int>>res) {
		 if (!node) return;
		 out.push_back(node->val);
		 if (sum == node->val && !node->left && !node->right)
			 res.push_back(out);
		 help(node->left, sum - node->val, out, res);
		 help(node->right, sum - node->val, out, res);
		 out.pop_back();
	 }
 };
int main() {
	/*vector<int> i = {1, 2, 3, 4, 0};
	Solution s;
	vector<int> ans = s.singleNumber(i);
	cout<<ans[0]<<ans[1]<< endl;*/
	system("pause");
	return 0;
}