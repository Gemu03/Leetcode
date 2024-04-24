from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def print(self):
        print(self.val)
        if self.next:
            self.next.print()

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_num = self.get_num(l1)
        l2_num = self.get_num(l2)

        result = l1_num + l2_num

        return self.get_list(result)
    
    def get_num(self, l: Optional[ListNode]) -> int:
        num = 0
        i = 0
        while l:
            num += l.val * (10 ** i)
            i += 1
            l = l.next
        return num
    
    def get_list(self, num: int) -> Optional[ListNode]:
        if num == 0:
            return ListNode(0)
        
        head = None
        while num > 0:
            val = num % 10
            num = num // 10
            if not head:
                head = ListNode(val)
                current = head
            else:
                current.next = ListNode(val)
                current = current.next
        return head

l1 = ListNode(3, ListNode(2))
l1.print()

print()

l2 = ListNode(5, ListNode(6, ListNode(4)))
l2.print()

print()

sol = Solution()
print(sol.addTwoNumbers(l1, l2).print())