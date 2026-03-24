# Delete all occurance of a key from dll

class Node:
    def __init__(self,value):
        self.val=value
        self.next=None
        self.prev=None

def createDLL(arr):
    if not arr:
        return None
    head=Node(arr[0])
    current_node=head
    for i in range(1,len(arr)):
        new_node=Node(arr[i])
        current_node.next=new_node
        new_node.prev=current_node
        current_node=new_node

    return head

def main():
    arr=list(map(int,input().split(" ")))
    key=int(input())
    head=createDLL(arr)
    ans=delete_key(head,key)
    curr=ans
    while curr is not None:
        print(curr.val,end=" ")
        curr=curr.next

    return

def delete_key(head,key):
    if head.next is None and head.val==key:
        return None
    
    prev_node=None
    curr_node=head
    new_head=head

    while curr_node is not None:
        if curr_node.val==key:
            if prev_node is not None:
                prev_node.next=curr_node.next
            if curr_node.next is not None:
                curr_node.next.prev=prev_node
            if curr_node==new_head:
                new_head=new_head.next
        prev_node=curr_node
        curr_node=curr_node.next

    return new_head



if __name__=="__main__":
    main()

