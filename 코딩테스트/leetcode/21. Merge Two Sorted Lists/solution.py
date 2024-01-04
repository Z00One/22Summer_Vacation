# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getValues(self, li: Optional[ListNode]) -> List[int]:
        temp = li
        output = []
        
        while temp:
            output.append(temp.val)
            temp = temp.next
        
        return output

    def makeToListNode(self, li: List[int]) -> Optional[ListNode]:
        list_node = None

        for e in li:
            list_node = ListNode(e, list_node)

        return list_node

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        li1, li2 = self.getValues(list1), self.getValues(list2)
        li = sorted((li1 + li2), reverse=True)
        return self.makeToListNode(li)