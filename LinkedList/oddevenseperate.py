#This is leet code 328 problem

#the below is brute force approach
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        temp=head
        lst=[]
        while temp is not None:
            lst.append(temp.val)
            if temp.next is not None:
                temp=temp.next.next
            else:
                break
        print(f'list after adding odd {lst}')
        temp=head.next
        while temp is not None:
            lst.append(temp.val)
            if temp.next is not None:
                temp=temp.next.next
            else:
                break
        print(f'lst {lst}')
        dummy=head
        count=0
        while dummy is not None:
            dummy.val=lst[count]
            count+=1
            dummy=dummy.next
        return head
    
#optimize way 
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        odd=head
        even=head.next
        even_head=even

        while even is not None and even.next is not None:
            odd.next=odd.next.next
            odd=odd.next
            even.next=even.next.next
            even=even.next
        odd.next=even_head
        return head