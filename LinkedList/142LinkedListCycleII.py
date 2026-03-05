# Brute force approach
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dit={}
        temp=head
        while temp is not None:
            if temp in dit:
                dit[temp]=dit.get(temp,1)+1
                break
            dit[temp]=1
            temp=temp.next
        for key in dit:
            if dit[key]>1:
                return key
        return None
    
#optimal solution is
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                slow=head
                while slow!=fast:
                    slow=slow.next
                    fast=fast.next
                return slow
        return None
    
#here we calculate the distance travelled by slow and fast and and once fast catches the slow the we make the
#slow equal head and we increment one by one each slow and fast and again once they are equal that will be 
#their meeting point