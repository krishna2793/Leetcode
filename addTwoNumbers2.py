# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        Itr1 = l1
        Itr2 = l2
        st1 = l1
        st2 = l2
        ret = None
        def recurse(l1,l2,s1,s2):
            if (l1 is None) and (l2 is None):
                return 0,None
            reminder = 0
            if (l1 == s1) and (l2==s2):
                if (l1 is None) or (l2 is None):
                    return 0,None
                reminder,nextItr = recurse(l1.next,l2.next,s1.next,s2.next)
                add = l1.val+l2.val+reminder
            elif l1 == s1:
                reminder,nextItr = recurse(l1,l2.next,s1,s2)
                add = l2.val+reminder
            elif l2 == s2:
                reminder,nextItr = recurse(l1.next,l2,s1,s2)
                add = l1.val+reminder
            if add>9:
                reminder = 1
            else:
                reminder = 0
            ret = ListNode(add%10)
            ret.next = nextItr
            return reminder,ret
        while not((Itr1 is None) and (Itr2 is None)):
            if Itr1 is None:
                st2 = st2.next
            else:
                Itr1=Itr1.next
            if Itr2 is None:
                st1 = st1.next
            else:
                Itr2=Itr2.next
        print()
        print(st1.val,st2.val)
        reminder,nextItr = recurse(l1,l2,st1,st2)
        if reminder >0:
            ret = ListNode(reminder)
            ret.next = nextItr
        else:
            ret = nextItr
        return ret