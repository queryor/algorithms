/*************************************************************************
	> File Name: ReverseList.cpp
	> Author: 
	> Mail: 
	> Created Time: 三  1/10 11:54:15 2018
 ************************************************************************/

#include<iostream>
using namespace std;

// 题目描述
// 输入一个链表，反转链表后，输出链表的所有元素。

// 解题思路 头插法：遍历链表的过程中，依次插为链表的头

/*
struct ListNode {
	int val;
	struct ListNode *next;
	ListNode(int x) :
			val(x), next(NULL) {
	}
};*/
class Solution {
public:
    ListNode* ReverseList(ListNode* pHead) {
       	ListNode* head=NULL;
        ListNode* p=pHead;
        while(p!=NULL){
            ListNode* temp = p->next;
            p->next = head;
            head = p;
            p = temp;
        }
        return head;
        
            
	
    }
};

