# Definition for singly-linked list.
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
        l1_pointer, l2_pointer, result_pointer = l1, l2, result  # Set initial pointer

        extra_node = None
        is_node = lambda x: x is not None

        while True:
            total = sum(
                [
                    node.val
                    for node in [l1_pointer, l2_pointer, extra_node]
                    if is_node(node)
                ]
            )
            q, r = divmod(total, 10)
            result_pointer.val = r

            extra_node = None
            if q:
                extra_node = ListNode(q)

            # Update pointer
            l1_pointer = l1_pointer.next if hasattr(l1_pointer, "next") else None
            l2_pointer = l2_pointer.next if hasattr(l2_pointer, "next") else None

            if not any([l1_pointer, l2_pointer, extra_node]):
                break

            result_pointer.next = ListNode()
            result_pointer = result_pointer.next
        return result
