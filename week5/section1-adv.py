# Problem 1: Villager Class， Problem 2: Add Furniture
#class Villager:
#    def __init__(self, name, species, catchphrase):
#        self.name = name
#        self.species = species
#        self.catchphrase = catchphrase
#        self.furniture = []
#
#    def add_item(self, item_name):
#        valid_items = [
#            "acoustic guitar",
#            "ironwood kitchenette",
#            "rattan armchair",
#            "kotatsu",
#            "cacao tree"
#        ]
#        if item_name in valid_items:
#            self.furniture.append(item_name)
#    
#
#apollo = Villager("Apollo", "Eagle", "pah")
#print(apollo.name)
#print(apollo.species) 
#print(apollo.catchphrase)
#print(apollo.furniture)
#
#alice = Villager("Alice", "Koala", "guvnor")
#print(alice.furniture)
#
#alice.add_item("acoustic guitar")
#print(alice.furniture)
#
#alice.add_item("cacao tree")
#print(alice.furniture)
#
#alice.add_item("nintendo switch")
#print(alice.furniture)

# Problem 3: Group by Personality
#class Villager:
#    def __init__(self, name, species, personality, catchphrase):
#        self.name = name
#        self.species = species
#        self.personality = personality
#        self.catchphrase = catchphrase
#        self.furniture = []
#    
#    def add_item(self, item_name):
#        valid_items = [
#            "acoustic guitar",
#            "ironwood kitchenette",
#            "rattan armchair",
#            "kotatsu",
#            "cacao tree"
#        ]
#        if item_name in valid_items:
#            self.furniture.append(item_name)
#
#def of_personality_type(townies, personality_type):
#    res = []
#    for v in townies:
#        if v.personality == personality_type:
#            res.append(v.name)
#    return res
#
#isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
#bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
#stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")
#
#print(of_personality_type([isabelle, bob, stitches], "Lazy"))
#print(of_personality_type([isabelle, bob, stitches], "Cranky"))

# Problem 4: Telephone
class Villager:
    def __init__(self, name, species, personality, catchphrase, neighbor=None):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []
        self.neighbor = neighbor
    
    def add_item(self, item_name):
        valid_items = [
            "acoustic guitar",
            "ironwood kitchenette",
            "rattan armchair",
            "kotatsu",
            "cacao tree"
        ]
        if item_name in valid_items:
            self.furniture.append(item_name)

def of_personality_type(townies, personality_type):
    res = []
    for v in townies:
        if v.personality == personality_type:
            res.append(v.name)
    return res

def message_received(start_villager, target_villager):
    while start_villager.neighbor:
        nei = start_villager.neighbor
        if nei == target_villager:
            return True
        start_villager = nei
    return False

isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
tom_nook = Villager("Tom Nook", "Raccoon", "Cranky", "yes, yes")
kk_slider = Villager("K.K. Slider", "Dog", "Lazy", "dig it")
isabelle.neighbor = tom_nook
tom_nook.neighbor = kk_slider

print(message_received(isabelle, kk_slider))
print(message_received(kk_slider, isabelle))

# Problem 5: Linked Up
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

# Problem 6: Got One!
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
    if head is None:
        print("Aw! Better luck next time!")
        return None
    else:
        print(f"I caught a {head.fish_name}!")
        return head.next
    
fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
empty_list = None

print_linked_list(fish_list)
print_linked_list(catch_fish(fish_list))
print(catch_fish(empty_list))

# Problem 7: Fishing Probability
class Node:
    def __init__(self, fish_name, next=None):
        self.fish_name = fish_name
        self.next = next

# For testing
import math
def print_linked_list(head):
    current = head
    while current:
        print(current.fish_name, end=" -> " if current.next else "\n")
        current = current.next

def fish_chances(head, fish_name):
    total = 0
    match = 0
    while head:
        total += 1
        if head.fish_name == fish_name:
            match += 1
        head = head.next
    
    if match == 0:
        return 0.00
    else:
        return math.floor((match / total) * 100) / 100


fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
print(fish_chances(fish_list, "Dace"))
print(fish_chances(fish_list, "Rainbow Trout"))

# Problem 8: Restocking the Lake
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

def restock(head, new_fish):
    new_node = Node(new_fish)
    if head is None:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head

fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
print_linked_list(restock(fish_list, "Rainbow Trout"))