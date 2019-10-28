# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        reminder = 0
        Itr1 = l1
        Itr2 = l2
        ret = Itr3 = None
        while (Itr1 != None) or (Itr2 != None):
            add = reminder
            if Itr1 is not None:
                add+=Itr1.val
            if Itr2 is not None:
                add+=Itr2.val
            if add>=10:
                add = add%10
                reminder = 1
            else:
                reminder = 0
            if ret is None:
                ret = ListNode(add)
                Itr3 = ret
            else:
                Itr3.next = ListNode(add)
                Itr3 = Itr3.next
            if Itr1 is not None:
                Itr1 = Itr1.next
            if Itr2 is not None:
                Itr2 = Itr2.next
        if reminder>0:
            Itr3.next = ListNode(reminder)
        return ret