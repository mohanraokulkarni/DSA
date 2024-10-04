# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if not head or not head.next:
            return False
        
        
        a=head
        b=head.next
        flag=0
        
        while b and b.next:
            a=a.next
            b=b.next.next 
            if a==b:
                flag=1
                break
        if flag==1:
            return True
        if flag==0:
            return False
        
        
