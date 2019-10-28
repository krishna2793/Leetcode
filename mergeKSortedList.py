# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        K = len(lists)
        Itr = [None]*K
        for i in range(K):
            Itr[i] = lists[i] 
        ret = ListNode(0)
        retItr = ret
        while any(itr is not None for itr in Itr):
            curr = sys.maxsize
            currK = 0
            for i in range(K):
                if Itr[i] is not None:
                    if Itr[i].val<curr:
                        curr = Itr[i].val
                        currK = i
            retItr.next = ListNode(Itr[currK].val)
            retItr = retItr.next
            Itr[currK] = Itr[currK].next
        return ret.next