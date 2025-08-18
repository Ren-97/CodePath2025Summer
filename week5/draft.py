class Villager:
    def __init__(self, name, species, personality, catchphrase, neighbor=None):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []
        self.neighbor = neighbor
    
    def add_item(self, item_name):
        valid = ["acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"]
        if item_name in valid:
            self.furniture.append(item_name)
        
def of_personality_type(townies, personality_type):
    res = []
    for v in townies:
        if v.personality == personality_type:
            res.append(v.name)
    return res

def message_received(start_villager, target_villager):
    if start_villager == target_villager:
        return True
    while start_villager.neighbor:
        nei = start_villager.neighbor
        if nei == target_villager:
            return True
        start_villager = nei
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

kk_slider = Node("K.K. Slider")
harriet = Node("Harriet")
saharah = Node("Saharah")
isabelle = Node("Isabelle")
kk_slider.next = harriet
harriet.next = saharah
saharah.next = isabelle

print_linked_list(kk_slider)

class Node:
    def __init__(self, fish_name, next=None):
        self.fish_name = fish_name
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.fish_name, end=" -> " if current.next else "\n")
        current = current.next

def catch_fish(head):
    if not head:
        print('Aw! Better luck next time!')
        return None
    else:
        print(f"I caught a {head.fish_name}!")
        return head.next
    
def fish_chances(head, fish_name):
    if not head:
        return 0
    total, match = 0, 0
    while head:
        total += 1
        if head.fish_name == fish_name:
            match += 1
        head = head.next
    return round(match / total,2)

def restock(head, new_fish):
    cur = head
    while cur.next:
        cur = cur.next
    cur.next = Node(new_fish)
    return head

fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
print_linked_list(restock(fish_list, "Rainbow Trout"))
    
