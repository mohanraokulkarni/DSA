# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if not head or not head.next:
            return False
        
        #head are always none type , it means there are locations 
        a=head
        b=head.next
        
        while b and b.next:
            a=a.next
            b=b.next.next 
            if a==b:
                return True
        return False
        
        
