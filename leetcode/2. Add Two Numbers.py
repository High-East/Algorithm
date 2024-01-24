from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        result = ListNode()
        pointer = result
        storage = 0

        while True:
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0
            storage, pointer.val = divmod(val1 + val2 + storage, 10)

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

            if (l1 is None) and (l2 is None) and not storage:
                break
            pointer.next = ListNode()
            pointer = pointer.next

        return result
