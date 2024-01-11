# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def makeToList(self, head: Optional[ListNode], li):
        li.append(head.val)
        if not head.next:
            return
        self.makeToList(head.next, li)

    def makeToListNode(self, li) -> Optional[ListNode]:
        list_node = None
        for v in li[::-1]:
            list_node = ListNode(v, list_node)

        return list_node
            
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        li = []
        self.makeToList(head, li)
        if(len(li) == 1):
            return None
        
        n = len(li) - n
        li = li[:n] + li[n+1:]
        
        ans = self.makeToListNode(li)

        return ans