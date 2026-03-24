# Give a target example 7 find the pairs whose sum is equal to target from given double linked list
#It will be a sorted linked list and also we have no duplicate values in it
class Node:
    def __init__(self,value):
        self.val=value
        self.prev=None
        self.next=None

def makeLinkedList(arr):
    if not arr:
        return None
    head=Node(arr[0])
    curr_node=head
    for i in range(1,len(arr)):
        new_node=Node(arr[i])
        curr_node.next=new_node
        new_node.prev=curr_node
        curr_node=curr_node.next

    return head

def brute(head,target): # here time is O(N*N) 
    target1=head
    ans=[]
    while target1 is not None:
        target2=target1.next
        while target2 is not None:
            if target1.val+target2.val==target:
                ans.append([target1.val,target2.val])
            target2=target2.next
        target1=target1.next

    print(f'ans in brute force{ans}')
    return ans

def better(head,target): #Here time is O(N) and space is O(N)
    set_values=set()
    curr=head
    ans=[]
    while curr is not None:
        rem=target-curr.val
        if rem in set_values:
            ans.append([rem,curr.val])
        set_values.add(curr.val)
        curr=curr.next

    print(f'ans in better {ans}')
    return ans

def optimal(head,target):
    right=head
    left=head
    ans=[]
    while right.next is not None:
        right=right.next

    while left is not None and right is not None and left.val<right.val:
        total=left.val+right.val
        if total==target:
            ans.append([left.val,right.val])
            left=left.next
            right=right.prev
        elif total>target:
            right=right.prev
        else:
            left=left.next

    print(f'optimal way result{ans}')
    return ans

def main():
    arr=[1,2,4,5,6,8,9]
    target=7
    head=makeLinkedList(arr)
    answer=brute(head,target)
    answer=better(head,target)
    answer=optimal(head,target)
    return answer

    

if __name__=="__main__":
    main()
