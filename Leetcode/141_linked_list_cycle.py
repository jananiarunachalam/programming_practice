from typing import Optional

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def has_cycle(head: Optional[ListNode]) -> bool:
    """Given a head node of a linkedlist
    return true if there's a cycle in the linkedlist 
    otherwise return false
    
    Args:
        head (ListNode)

    Returns:
        bool
    """
    if not head: return False

    fast, slow = head.next, head
    update_slow = False

    while fast and fast != slow:
        fast = fast.next

        if update_slow := not update_slow:
            slow = slow.next

    return fast == slow