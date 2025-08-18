class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def find_max(head):
    if not head:
        return None
    max_ = -float('inf')
    while head:
        max_ = max(max_, head.value)
        head = head.next
    return max_

def remove_tail(head):
    if head is None:
        return None
    if head.next is None:
        return None 
        
    current = head
    while current.next.next: 
        current = current.next

    current.next = None 
    return head

def delete_dupes(head):
    prev = dummy = Node(0)
    cur = dummy.next = head
    
    while cur:
        has_dup = False
        while cur.next and cur.value == cur.next.value:
            has_dup = True
            cur = cur.next
        if has_dup:
            prev.next = cur.next
        else:
            prev = cur
        cur = cur.next
    return dummy.next

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def has_cycle(head):
    fast = slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def remove_nth_from_end(head, n):
    dummy = Node(0)
    dummy.next = head
    slow = fast = dummy
    for i in range(n+1):
        fast = fast.next
    while fast:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return dummy.next
    
#head1 = Node("apple", Node("cherry", Node("orange", Node("peach", Node("pear")))))
#head2 = Node("Rainbow Trout", Node("Ray"))
#head3 = Node("Rainbow Stag")
#
#
#print_linked_list(remove_nth_from_end(head1, 2))
#print_linked_list(remove_nth_from_end(head2, 1))
#print_linked_list(remove_nth_from_end(head3, 1))

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next
        
def reverse_first_k(head, k):
    if not head:
        return None
    count = 0
    prev = None
    cur = head
    while head and count != k:
        count += 1
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp
    
    head.next = cur
    return prev

head = Node("apple", Node("cherry", Node("orange", Node("peach", Node("pear")))))

print_linked_list(reverse_first_k(head, 3))