# Problem 1: Greatest Node, Problem 2: Remove Tail, Problem 3: Delete Duplicates in a Linked List
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
    res = -float('inf')
    if not head:
        return None
    while head:
        res = max(res, head.value)
        head = head.next
    return res

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
    dummy = Node(0)
    dummy.next = head
    prev, cur = dummy, dummy.next
    while cur:
        has_dupes = False
        while cur.next and cur.value == cur.next.value:
            has_dupes = True
            cur = cur.next
        
        if has_dupes:
            prev.next = cur.next
        else:
            prev = cur
        cur = cur.next

    return dummy.next

head = Node(1, Node(2, Node(3, Node(3, Node(5, Node(5))))))

# Linked List: 1 -> 2 -> 3 -> 3 -> 4 -> 5
print_linked_list(delete_dupes(head))

# Problem 4: Does it Cycle?
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def has_cycle(head):
    if not head:
        return False
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

peach = Node("Peach", Node("Luigi", Node("Mario", Node("Toad"))))

# Toad.next = Luigi
peach.next.next.next = peach.next

print(has_cycle(peach))

# Problem 5: Remove Nth Node From End of List
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
    fast = slow = dummy
    for i in range(n+1):
        fast = fast.next
    
    while fast:
        fast = fast.next
        slow = slow.next
    
    slow.next = slow.next.next
    return dummy.next

head1 = Node("apple", Node("cherry", Node("orange", Node("peach", Node("pear")))))
head2 = Node("Rainbow Trout", Node("Ray"))
head3 = Node("Rainbow Stag")


print_linked_list(remove_nth_from_end(head1, 2))
print_linked_list(remove_nth_from_end(head2, 1))
print_linked_list(remove_nth_from_end(head3, 1))


# Problem 6: Careful Reverse
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
    cur = head
    prev = None
    count = 0
    while cur and count != k:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp
        count += 1
    head.next = cur
    return prev

head = Node("apple", Node("cherry", Node("orange", Node("peach", Node("pear")))))

print_linked_list(reverse_first_k(head, 3)) 