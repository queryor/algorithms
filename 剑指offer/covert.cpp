// 题目描述
// 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
//要求不能创建任何新的结点，只能调整树中结点指针的指向。

//解题思路 中序遍历 然后依次将节点加入双向链表。 
#include<iostream>

struct TreeNode {
	int val;
	struct TreeNode *left;
	struct TreeNode *right;
	TreeNode(int x) :
			val(x), left(NULL), right(NULL) {
	}
};
class Solution {
public:
    TreeNode* Convert(TreeNode* pRootOfTree)
    {
        head = NULL;
        Convert_process(pRootOfTree);
        return head;
    }
    void Convert_process(TreeNode* p)
    {
        if(p!=NULL){
            Convert_process(p->left);
            add_p(p);
            Convert_process(p->right);
        }
    }
    void add_p(TreeNode* p)
    {
        if(head==NULL){
            head = p;
            end = p;
        }
        else{
            end->right = p;
            p->left = end;
            end = p;
        }
    }
    TreeNode* head = NULL;
    TreeNode* end = NULL;
};