# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getSortedValues(self, li: Optional[ListNode]) -> List[int]:
        temp = li
        output = []
        
        while temp:
            output.append(temp.val)
            temp = temp.next
        
        output.sort(reverse=True)
        return output

    def makeToListNode(self, li: List[int]) -> Optional[ListNode]:
        list_node = None

        for e in li:
            list_node = ListNode(e, list_node)

        return list_node

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sortedList = self.getSortedValues(head)
        return self.makeToListNode(sortedList)
        