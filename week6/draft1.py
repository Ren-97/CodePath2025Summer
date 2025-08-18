class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def cycle_length(protein):
    fast = slow = protein
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    res = [slow.value]
    fast = fast.next
    while fast != slow:
        res.append(fast.value)
        fast = fast.next
    return res


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    if not head:
        print("Empty List")
        return
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def split_protein_chain(protein, k):
    length = 0
    cur = protein
    while cur:
        length += 1
        cur = cur.next
    
    segment = length // k
    remainder = length % k

    cur = protein
    res = []
    for i in range(k):
        if i < remainder:
            size = segment + 1
        else:
            size = segment
        head = cur
        for j in range(size-1):
            cur = cur.next
        
        if cur:
            temp =cur.next
            cur.next = None
            cur = temp
        res.append(head)
    return res 

protein1 = Node('Ala', Node('Gly', Node('Leu', Node('Val', Node('Pro', Node('Ser', Node('Thr', Node('Cys'))))))))
protein2 = Node('Ala', Node('Gly', Node('Leu', Node('Val'))))

parts = split_protein_chain(protein1, 3)
for part in parts:
    print_linked_list(part)

parts = split_protein_chain(protein2, 5)
for part in parts:
    print_linked_list(part)

    