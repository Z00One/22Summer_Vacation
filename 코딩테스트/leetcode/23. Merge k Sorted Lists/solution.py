# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def makeToList(self, li: Optional[ListNode]):
        if not li:
            return []
        
        l = []
        while True:
            l.append(li.val)
            li = li.next
            if not li:
                return l

    def makeToListNode(self, li: List[int]) -> Optional[ListNode]:
        list_node = None

        for e in li:
            list_node = ListNode(e, list_node)

        return list_node

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None
        
        li = []
        for l in lists:
            li += self.makeToList(l)
        li.sort(reverse=True)
        li = self.makeToListNode(li)

        return li