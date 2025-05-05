from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val

def reverseBetween(self, head, left, right):
    """
    :type head: Optional[ListNode]
    :type left: int
    :type right: int
    :rtype: Optional[ListNode]
    """
    dummy = ListNode(next = head)
    p0 = dummy

    for _ in range(left-1):
        p0 = p0.next    # 这时候p0指的是left的node的前一个node
    
    pre = None
    cur = p0.next
    for _ in range(right-left+1):
        nxt = cur.next
        cur.next = pre

        pre = cur
        cur = nxt

    p0.next.next = cur
    p0.next = pre

    return dummy.next