from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseKGroup(self, head, k):
    """
    :type head: Optional[ListNode]
    :type k: int
    :rtype: Optional[ListNode]
    """
    # 求链表长度
    n = 0
    cur = head
    while cur:
        n += 1
        cur = cur.next

    dummy = ListNode(next=head)
    p0 = dummy
    pre = None
    cur = p0.next

    while n >= k:
        n -= k
        for _ in range(k):
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        
        # 先存下原始的p0的next
        nxt = p0.next
        # 更新p0
        p0.next = pre
        p0.next.next = cur
        p0 = nxt

    return dummy.next
