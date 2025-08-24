# Problem 1: Next in Queue
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

# For testing
def print_queue(head):
    current = head.front
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def is_empty(self):
        return self.front is None

    def enqueue(self, song_tuple):
        new_node = Node(song_tuple)
        if self.is_empty():
             self.front = new_node
             self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
    
    def dequeue(self):
        if self.is_empty():
             return None
        remove_val = self.front.value
        self.front = self.front.next
        return remove_val
    
    def peek(self):
        if self.is_empty():
             return None
        return self.front.value
    
"""
# Create a new Queue
q = Queue()

# Add elements to the queue
q.enqueue(('Love Song', 'Sara Bareilles'))
q.enqueue(('Ballad of Big Nothing', 'Elliot Smith'))
q.enqueue(('Hug from a Dinosaur', 'Torres'))
print_queue(q)

# View the front element
print("Peek: ", q.peek()) 

# Remove elements from the queue
print("Dequeue: ", q.dequeue()) 
print("Dequeue: ", q.dequeue()) 

# Check if the queue is empty
print("Is Empty: ", q.is_empty()) 

# Remove the last element
print("Dequeue: ", q.dequeue()) 

# Check if the queue is empty
print("Is Empty:", q.is_empty())
"""

# Problem 2: Merge Playlists
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

def merge_playlists(playlist1, playlist2, a, b):
    dummy = Node(0, playlist1)
    prev_a = dummy
    for _ in range(a):
         prev_a = prev_a.next

    cur = prev_a
    for _ in range(b-a+2):
         cur = cur.next
    #after_b = cur

    tail = playlist2
    while tail.next:
         tail = tail.next

    prev_a.next = playlist2
    tail.next = cur
    return dummy.next
             
"""
playlist1 = Node(('Flea', 'St. Vincent'),
                Node(('Juice', 'Lizzo'), 
                    Node(('Tenderness', 'Jay Som'),
                        Node(('Ego Death', 'The Internet'),
                            Node(('Empty', 'Kevin Abstract'))))))

playlist2 = Node(('Dreams', 'Solange'), Node(('First', 'Gallant')))

print_linked_list(merge_playlists(playlist1, playlist2, 2, 3))
"""

# Problem 3: Shuffle Playlist
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

def shuffle_playlist(playlist):
    slow, fast = playlist, playlist.next
    while fast and fast.next:
          slow = slow.next
          fast = fast.next.next
    prev = None
    cur = slow.next
    slow.next = None

    while cur:
         temp = cur.next
         cur.next = prev
         prev = cur
         cur = temp
    
    first, second = playlist, prev
    while second:
         temp1, temp2 = first.next, second.next
         first.next = second
         second.next = temp1
         first, second = temp1, temp2
    return playlist     

"""
playlist1 = Node(1, Node(2, Node(3, Node(4))))

playlist2 = Node(('Respect', 'Aretha Franklin'),
                Node(('Superstition', 'Stevie Wonder'),
                    Node(('Wonderwall', 'Oasis'),
                        Node(('Like a Prayer', 'Madonna'),
                            Node(('Bohemian Rhapsody', 'Queen'))))))

print_linked_list(shuffle_playlist(playlist1))
print_linked_list(shuffle_playlist(playlist2))
"""

# Problem 4: Shared Music Taste
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

def playlist_overlap(playlist_a, playlist_b):
    a, b = playlist_a, playlist_b
    while a != b:
         a = a.next if a else playlist_b
         b = b.next if b else playlist_a
    return a

"""
playlist_a = Node('Song A', Node('Song B'))
playlist_b = Node('Song X', Node('Song Y', Node('Song Z')))
shared_segment = Node('Song M', Node('Song N', Node('Song O')))

playlist_a.next.next = shared_segment
playlist_b.next.next.next = shared_segment

print((playlist_overlap(playlist_a, playlist_b)).value)
"""

# Problem 5: Double Listening Count
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

# Method 1
def double_listeners(monthly_listeners):
    prev, cur = None, monthly_listeners
    while cur:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp

    cur = prev
    carry = 0
    while cur:
        total = cur.value * 2 + carry
        carry = total // 10
        cur.value = total % 10
        if not cur.next and carry:
            cur.next = Node(carry)
            break
        cur = cur.next

    prev2 , cur = None, prev  
    while cur:
        temp = cur.next
        cur.next = prev2
        prev2 = cur
        cur = temp 
    return prev2

# Method 2
def double_listeners(monthly_listeners):
    def dfs(node):
        if not node:
             return 0
        carry = dfs(node.next)
        total = node.value * 2 + carry
        node.value = total % 10
        return total // 10
    
    carry = dfs(monthly_listeners)
    if carry:
        new_head = Node(carry, monthly_listeners)
        return new_head
    return monthly_listeners

"""    
monthly_listeners1 = Node(1, Node(8, Node(9))) # 189
monthly_listeners2 = Node(9, Node(9, Node(9))) # 999

print_linked_list(double_listeners(monthly_listeners1))
print_linked_list(double_listeners(monthly_listeners2))
"""
