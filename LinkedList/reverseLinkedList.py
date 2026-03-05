class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node=None
        curr_node=head
        while curr_node is not None:
            front_node=curr_node.next
            curr_node.next=prev_node
            prev_node=curr_node
            curr_node=front_node

        return prev_node

#here for reverse linked list we initialize prev_node to None and curr_node to head
#after that we take front_node as curr_node.next and curr_node to prev_node which will be none in first itertaion
#after that we update prev_node with curr_node and then after that we update curr_node with next_node
        