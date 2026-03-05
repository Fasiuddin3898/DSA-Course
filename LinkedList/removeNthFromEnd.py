#Brute force approach to remove the nth node from the end of the linked list
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None and n==1:
            return None
        if head is None:
            return None
        length=0
        temp=head
        while temp is not None:
            length+=1
            temp=temp.next
        print(f'length of linked list {length}')
        remove=length-n+1
        prev_node=None
        curr_node=head
        count=1
        found=False
        while curr_node is not None:
            if count==remove:
                found=True
                break
            prev_node=curr_node
            curr_node=curr_node.next
            count+=1
        print(f'remove {remove}')
        if found:
            if remove==1:
                head=head.next
                return head
            prev_node.next=curr_node.next
            del curr_node
        return head
    
#optimal solution to remove the nth node from the end of linked list
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow=head
        fast=head
        for _ in range(n):
            fast=fast.next
        if fast is None:
            return head.next
        while fast.next is not None:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next
        return head