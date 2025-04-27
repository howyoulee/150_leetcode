def reverseList(self, head):
    """
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    prev = None  # 初始化 prev 为 None，表示反转后链表的尾部
    cur = head  # 当前节点从 head 开始

    while cur:
        nxt = cur.next  # 标记下一个节点为全局标记 nxt
        cur.next = prev  # 当前节点的指针指向 prev，反转指针方向
        prev = cur  # 把全局标记 prev 给 cur
        cur = nxt  # 把全局标记 cur 给 nxt，移动到下一个节点

    return prev  # 返回反转后的新头节点

