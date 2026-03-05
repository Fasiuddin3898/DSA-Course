#Brute force using dict find out the linked list is cycle or not 
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dit={}
        curr_node=head
        while curr_node is not None:
            if curr_node in dit:
                return True
            dit[curr_node]=dit.get(curr_node,1)+1
            curr_node=curr_node.next
        return False
    
#Optimal solution for linked list is cycel or not

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False
    
#in optimal solution also we follow the same thing which was followed in TortoiseHare