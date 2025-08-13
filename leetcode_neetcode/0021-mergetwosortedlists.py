# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:
# Input: list1 = [], list2 = []
# Output: []

# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


list1values = [1,2,4]
list2values = [1,3,4]

list1head = ListNode()
list2head = ListNode()

current = list1head
for val in list1values:
    current.val = val
    current.next = ListNode()
    current = current.next

current = list2head
for val in list2values:
    current.val = val
    current.next = ListNode()
    current = current.next

def print_linkedlist(head):
    temp = head
    while temp.val !=0 :
        print(temp.val)
        temp = temp.next

print('list1 values:')
print(print_linkedlist(list1head))
print('list 2 values:')
print(print_linkedlist(list2head))

def merge_sorted_list(list1, list2):
    head = ListNode()
    temp = head
    while list1.next or list2.next:
        if list1.val < list2.val:
                temp.val = list1.val
                temp.next = ListNode()
                temp = temp.next
        else:
            temp.val = list2.val
            temp.next = ListNode()
            temp = temp.next
    return head

print(print_linkedlist(merge_sorted_list(list1head, list2head)))
