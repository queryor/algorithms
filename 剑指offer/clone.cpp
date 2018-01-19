

// 题目描述
// 输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），
// 返回结果为复制后复杂链表的head。
// （注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）

/*
struct RandomListNode {
    int label;
    struct RandomListNode *next, *random;
    RandomListNode(int x) :
            label(x), next(NULL), random(NULL) {
    }
};
*/
class Solution {
public:
    RandomListNode* Clone(RandomListNode* pHead)
    {
        clonenode(pHead);
        conectnode(pHead);
        return divinode(pHead);
    }
    void clonenode(RandomListNode* pHead)
    {
        RandomListNode* p = pHead;
        while(p!=NULL){
            RandomListNode* node = new RandomListNode(p->label);
            node->next = p->next;
            p->next = node;
            p = node->next;
        }
    }
    void conectnode(RandomListNode* pHead)
    {
        RandomListNode* p = pHead;
        while(p!=NULL){
            if(p->random!=NULL){
                p->next->random=p->random->next;
            }
            p=p->next->next;
        }
    }
    RandomListNode* divinode(RandomListNode* pHead)
    {
        if(pHead==NULL)return NULL;
        RandomListNode *head=pHead->next;
        RandomListNode *p=pHead->next->next,*p1=head;
        pHead->next = p;
        while(p!=NULL){
            p1->next = p->next;
            p->next = p->next->next;
            p = p->next;
            p1=p1->next;
        }
        p1->next = NULL;
        return head;

    }
};