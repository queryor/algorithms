/*******************
 * 
 * 题目描述
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
 * 
 * 
 ****************/

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

    /****************
     递归版本 
     * 
     ******************/ 
    ListNode* Merge(ListNode* pHead1, ListNode* pHead2)
    {
        if(pHead2==NULL){
            return pHead1;
        }
        if(pHead1==NULL){
            return pHead2;
        }
       	if(pHead1->val<=pHead2->val){
            pHead1->next=Merge(pHead1->next,pHead2);
            return pHead1;
        }
        else
        {
            pHead2->next=Merge(pHead1,pHead2->next);
            return pHead2;
        }
    }


    ListNode* Merge(ListNode* pHead1, ListNode* pHead2)
    {
        if(!pHead1)
            return pHead2;
        if(!pHead2)
            return pHead1;
        ListNode* Head;
        ListNode* p;
        //取较小值作头结点
        if(pHead1->val<=pHead2->val){
            Head=pHead1;
            pHead1=pHead1->next;
        }
        else{
            Head=pHead2;
            pHead2=pHead2->next;
        }  
        //开始遍历合并
        p=Head;                                                   //p为合并后的链表的工作指针
        while(pHead1!=NULL&&pHead2!=NULL){                       //当有一个链表到结尾时，循环结束
            if(pHead1->val<=pHead2->val){          //如果链表1的结点小于链表2的结点
                p->next=pHead1;                            //取这个结点加入合并链表
                pHead1=pHead1->next;                 //链表1后移一位
                p=p->next;                                      //工作指针后移一位
            }               
            else{                                               //否则取链表2的结点
                p->next=pHead2;
                pHead2=pHead2->next;
                p=p->next;
            }                
        }
        if(pHead1 == NULL)           //链表1遍历完了
            p->next = pHead2;         //如果链表2也遍历完了，则pHead2=NULL
        if(pHead2 == NULL)            //链表2遍历完了
            p->next = pHead1;         ///如果链表1也遍历完了，则pHead1=NULL
        return Head;
        
    }
    
};