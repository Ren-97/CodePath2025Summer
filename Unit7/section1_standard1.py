# Problem 1: Counting Iron Man's Suits
def count_suits_iterative(suits):
     count = 0
     for suit in suits:
         count+=1
     return count
def count_suits_recursive(suits):
    if suits == []:
        return 0
    return 1 + count_suits_recursive(suits[1:]) 

"""
print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark I", "Mark III", "Mark IV"]))
"""

# Problem 2: Collecting Infinity Stones
def sum_stones(stones):
    if stones == []:
        return 0
    return stones[0] + sum_stones(stones[1:])

"""
print(sum_stones([5, 10, 15, 20, 25, 30]))
print(sum_stones([12, 8, 22, 16, 10]))
"""

# Problem 3: Counting Unique Suits
def count_suits_iterative(suits):
    set_ = set()
    for suit in suits:
        set_.add(suit)
    return len(set_)

def count_suits_recursive(suits):
    def helper(suits, set_):
        if suits == []:
            return len(set_)
        set_.add(suits[0])
        return helper(suits[1:], set_)
    return helper(suits, set())

"""
print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark I", "Mark III"]))
"""

# Problem 4: Calculating Groot's Growth
def fibonacci_growth(n):
    if n <= 1:
        return n
    return fibonacci_growth(n-1) + fibonacci_growth(n-2)

"""
print(fibonacci_growth(5))
print(fibonacci_growth(8))
"""

# Problem 5: Calculating the Power of the Fantastic Four
def power_of_four(n):
    if n == 0:
        return 1

    if n > 0:
        return 4 * power_of_four(n-1)
    # else:
    #     return 1 / (power_of_four(-n))
    if n < 0:
        return 1 / 4 * power_of_four(n+1)

"""    
print(power_of_four(2)) 
print(power_of_four(-2))
"""

# Problem 6: Strongest Avenger
def strongest_avenger(strengths):
    def helper(strengths, max):
        if strengths == []:
            return max
        if strengths[0] > max:
            max = strengths[0]
        return helper(strengths[1:], max)
    return helper(strengths, float("-inf"))


def strongest_avenger(strengths):
    if len(strengths) == 1:
        return strengths[0]
    rest_max = strongest_avenger(strengths[1:])
    if strengths[0] > rest_max:
        return strengths[0]
    else:
        return rest_max

"""
print(strongest_avenger([88, 92, 95, 99, 97, 100, 94]))
print(strongest_avenger([50, 75, 85, 60, 90]))
"""

# Problem 7: Counting Vibranium Deposits
def count_deposits(resources):
    if len(resources) == 0:
        return 0
    if resources[0] == "V":
        return 1 + count_deposits(resources[1:])
    else:
        return count_deposits(resources[1:]) 

"""
print(count_deposits("VVVVV"))
print(count_deposits("VXVYGA"))
"""

# Problem 8: Merging Missions
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

def merge_missions(mission1, mission2):
    if not mission1:
        return mission2
    if not mission2:
        return mission1
    if mission1.value <= mission2.value:
        mission1.next = merge_missions(mission1.next, mission2)
        return mission1
    else:
        mission2.next = merge_missions(mission1, mission2.next)
        return mission2
    
"""
mission1 = Node(1, Node(2, Node(4)))
mission2 = Node(1, Node(3, Node(4)))

print_linked_list(merge_missions(mission1, mission2))
"""

# Problem 9: Merging Missions II
class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def merge_missions_iterative(mission1, mission2):
    temp = Node()  # Temporary node to simplify the merging process
    tail = temp

    while mission1 and mission2:
        if mission1.value < mission2.value:
            tail.next = mission1
            mission1 = mission1.next
        else:
            tail.next = mission2
            mission2 = mission2.next
        tail = tail.next

    # Attach the remaining nodes, if any
    if mission1:
        tail.next = mission1
    elif mission2:
        tail.next = mission2

    return temp.next  # Return the head of the merged linked list