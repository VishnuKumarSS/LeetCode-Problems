from typing import Optional

# # Definition for singly-linked list.
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        if not list1 and list2:
            return list2
        if list1 and not list2:
            return list1

        temp_list2 = list2
        while temp_list2:
            temp_list1 = list1
            while temp_list1:
                if (temp_list2.val > temp_list1.val and temp_list2.val < temp_list1.next.val) or temp_list1.next is None:
                    temp = temp_list1
                    temp_list1.next = temp_list2
                    temp_list1.next.next = temp

                temp_list1 = list1.next

            temp_list2 = list2.next