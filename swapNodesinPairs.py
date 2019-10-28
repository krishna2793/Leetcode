# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if (head is not None) and (head.next is not None):
            Itr = head.next
            head.next = Itr.next
            Itr.next= head
            head = Itr
        else:
            return head
        
        Itr1 = head.next
            
        while (Itr1 is not None):
            Itr2 = Itr1.next
            if Itr2 is not None and Itr2.next is not None:
                Itr3 = Itr2.next
                Itr1.next = Itr2.next
                Itr2.next= Itr3.next
                Itr3.next = Itr2
            else:
                break
            Itr1 = Itr1.next.next
        return head 