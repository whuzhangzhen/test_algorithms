#coding:utf-8
'''
leetcode
tag:linkedlist
time：2017-7-14
@authorz:zhangzhen
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    #id:19
    # Given linked list: 1->2->3->4->5, and n = 2.
    # After removing the second node from the end, the linked list becomes 1->2->3->5.
    def removeNthFromEnd(self,head,n):
        '''
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        '''
        fast=slow=head
        for _ in range (n):
            fast=fast.next
        if not fast:
            return head.next
        while fast.next:
            fast=fast.next
            slow=slow.next
        slow.next=slow.next.next
        return head
    #id:160
    
    def getIntersectionNode(self, headA, headB):
         """
         :type head1, head1: ListNode
         :rtype: ListNode
         """
        #排除空链表
        if headA is None or headB is None:
            return None
        #定义两个遍历指针
        pa=headA
        pb=headB

        while pa is not pb:
            #两个链表各遍历两次
            #如果有相交则返回相交的位置，没有则返回None
            pa=headB if pa is None else pa.next
            pb=headA if pb is None else pb.next


        return pa
           

     def removeElements(self, head, val):
         """
         :type head: ListNode
         :type val: int
         :rtype: ListNode
         """
        if head is None:
            return None
        cur=head
        while cur is not None:
            if cur  if cur==val:
                cur=cur==val:
                cur=cur
                
     def reverseList(self, head):
         """
         :type head: ListNode
         :rtype: ListNode
         """
         prev=None
         while head :
             curr=head
             head=head.next
             curr.next=prev
             prev=curr
        return prev
    def deleteNode(self,node):
         '''
         :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
         '''
        
         if node is None or node.next is None:
                return 
                    
         else:
             node.val=node.next.val
             node.next=node.next.next 

    def addTwoNumbers(self,l1,l2):
        carry=0
        res=n=ListNode(0)
        while l1 or l2 or carry:
            if l1:
                carry+=l1.val
                l1=l1.next
           if l2:
               carry+=l2
               l2=l2.next
           carry,val=divmod(carry,10)
           n.next=ListNode(val)
           n=n.next
        return res.next

    def swapPairs(self,head):
        """
         :type head: ListNode
         :rtype: ListNode
         """
         pre,pre.next=slef,head
         while pre.next and pre.next.next:
             a=pre.next
             b=a.next
             pre.next=b
             b.next=a
             a.next=b.next
             pre=a
        return self.next
























