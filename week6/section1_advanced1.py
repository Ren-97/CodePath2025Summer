# Problem 1: Selective DNA Deletion
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

def edit_dna_sequence(dna_strand, m, n):
    cur = dna_strand
    while cur:
        for i in range(m-1):
            if cur is None:
                break
            cur = cur.next
        if cur is None:
            break
        temp = cur
        for j in range(n+1):
            if temp is None:
                break
            temp = temp.next

        cur.next = temp
        cur = cur.next
    return dna_strand

"""
dna_strand = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9, Node(10, Node(11, Node(12, Node(13)))))))))))))
print_linked_list(edit_dna_sequence(dna_strand, 2, 3))
"""

# Problem 2: Protein Folding Loop Detection
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
    fast = slow.next
    while slow != fast:
        res.append(fast.value)
        fast = fast.next
    return res

"""
protein_head = Node('Ala', Node('Gly', Node('Leu', Node('Val'))))
protein_head.next.next.next.next = protein_head.next 
print(cycle_length(protein_head))
"""

# Problem 3: Segmenting Protein Chains for Analysis
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
    
    partial_size = length // k 
    remainder = length % k
    res = []
    cur = protein
    for i in range(k):
        if i < remainder:
            size = partial_size + 1
        else:
            size = partial_size
        head = cur

        for _ in range(size-1):
            if cur:
                cur = cur.next
        
        if cur:
            temp = cur.next
            cur.next = None
            cur = temp

        res.append(head)
    return res

"""
protein1 = Node('Ala', Node('Gly', Node('Leu', Node('Val', Node('Pro', Node('Ser', Node('Thr', Node('Cys'))))))))
protein2 = Node('Ala', Node('Gly', Node('Leu', Node('Val'))))

parts = split_protein_chain(protein1, 3)
for part in parts:
    print_linked_list(part)

parts = split_protein_chain(protein2, 5)
for part in parts:
   print_linked_list(part)
"""

# Problem 4: Maximum Protein Pair Stability
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

def max_protein_pair_stability(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    cur = slow
    prev = None
    while cur:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp
    second = prev
    first = head
    max_sum = 0
    while second:
        max_sum = max(max_sum, first.value + second.value)
        first = first.next
        second = second.next
    return max_sum

"""
head1 = Node(5, Node(4, Node(2, Node(1))))
head2 = Node(4, Node(2, Node(2, Node(3))))

print(max_protein_pair_stability(head1))
print(max_protein_pair_stability(head2))
"""

# Problem 5: Grouping Experiments
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

def odd_even_experiments(exp_results):
    if not exp_results or not exp_results.next:
        return exp_results
    
    odd = exp_results
    even = exp_results.next
    evenhead = even

    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next
    odd.next = evenhead
    return exp_results

"""
experiment_results1 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
experiment_results2 = Node(2, Node(1, Node(3, Node(5, Node(6, Node(4, Node(7)))))))

print_linked_list(odd_even_experiments(experiment_results1))
print_linked_list(odd_even_experiments(experiment_results2))
"""