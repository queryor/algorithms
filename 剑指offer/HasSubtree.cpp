
// 题目描述
// 输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）

// 题解：先判断是不是以根节点为第一个点的子树，然后递归的查看左孩子和右孩子

/*
struct TreeNode {
	int val;
	struct TreeNode *left;
	struct TreeNode *right;
	TreeNode(int x) :
			val(x), left(NULL), right(NULL) {
	}
};*/
class Solution {
        bool isSubtree(TreeNode* pRootA, TreeNode* pRootB) {
        if (pRootB == NULL) return true;
        if (pRootA == NULL) return false;
        if (pRootB->val == pRootA->val) {
            return isSubtree(pRootA->left, pRootB->left)
                && isSubtree(pRootA->right, pRootB->right);
        } else return false;
    }
public:
    bool HasSubtree(TreeNode* pRoot1, TreeNode* pRoot2)
    {
		if(pRoot1==NULL || pRoot2==NULL)
            return false;
		return isSubtree(pRoot1, pRoot2) ||
            HasSubtree(pRoot1->left, pRoot2) ||
            HasSubtree(pRoot1->right, pRoot2);
    }
};