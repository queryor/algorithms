#include <iostream>
#include <unordered_set>
#include <algorithm>
#include <vector>
#include <string>
#include <numeric>
#include <queue>
#include <stack>
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
	 vector<int> preorderTraversal(TreeNode* root) {
		 if (!root) return{};
		 vector<int> res;
		 stack<TreeNode*> s{ { root } };
		 while (!s.empty()) {
			 TreeNode *t = s.top(); s.pop();
			 res.push_back(t->val);
			 if (t->right) s.push(t->right);
			 if (t->left) s.push(t->left);
		 }
		 return res;
	 }
 };

 class Solution1 {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> res;
        stack<TreeNode*> s;
        TreeNode *p = root;
        while (!s.empty() || p) {
            if (p) {
                s.push(p);
                res.push_back(p->val);
                p = p->left;
            } else {
                TreeNode *t = s.top(); s.pop();
                p = t->right;
            }
        }
        return res;
    }
};