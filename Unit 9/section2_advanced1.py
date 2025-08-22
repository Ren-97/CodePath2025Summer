# Problem 1: Creating Cookie Orders from Descriptions
from collections import deque 

# Tree Node class
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)

class TreeNode:
    def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right

def build_cookie_tree(descriptions):
    nodes = {}
    child_nodes = set()
    for node in descriptions:
        parent_flavor, child_flavor, is_left = node
        if parent_flavor not in nodes:
            nodes[parent_flavor] = TreeNode(parent_flavor)
            #start_node = nodes[parent_flavor]

        if child_flavor not in nodes:
            nodes[child_flavor] = TreeNode(child_flavor)
            child_nodes.add(child_flavor)

        if is_left:
            nodes[parent_flavor].left = nodes[child_flavor]
        else:
            nodes[parent_flavor].right = nodes[child_flavor]
        
    for flavor in nodes:
        if flavor not in child_nodes:
            return nodes[flavor]

"""
descriptions1 = [
    ["Chocolate Chip", "Peanut Butter", 1],
    ["Chocolate Chip", "Oatmeal Raisin", 0],
    ["Peanut Butter", "Sugar", 1]
]

descriptions2 = [
    ["Ginger Snap", "Snickerdoodle", 0],
    ["Ginger Snap", "Shortbread", 1]
]

# Using print_tree() function included at top of page
print_tree(build_cookie_tree(descriptions1))
print_tree(build_cookie_tree(descriptions2))
"""

# Problem 2: Cookie Sum
from collections import deque 

# Tree Node class
class TreeNode:
  def __init__(self, value, key=None, left=None, right=None):
      self.key = key
      self.val = value
      self.left = left
      self.right = right

def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def count_cookie_paths(root, target_sum):
    if not root:
        return 0
    if not root.left and not root.right:
        return 1 if root.val == target_sum else 0
   
    return count_cookie_paths(root.left, target_sum - root.val) + count_cookie_paths(root.right, target_sum - root.val)

"""
cookie_nums = [10, 5, 8, 3, 7, 12, 4]
cookies1 = build_tree(cookie_nums)
cookie_nums = [8, 4, 12, 2, 6, None, 10]
cookies2 = build_tree(cookie_nums)

print(count_cookie_paths(cookies1, 22)) 
print(count_cookie_paths(cookies2, 14))
"""

# Problem 3: Most Popular Cookie Combo
import collections

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def most_popular_cookie_combo(root):
    count = collections.defaultdict(int)
    if not root:
        return []
    
    def post_order(node):
        if not node:
            return 0
        left = post_order(node.left)
        right = post_order(node.right)
        total = left + right + node.val
        count[total] += 1
        return total
    
    post_order(root)
    max_count = max(count.values())
    res = []
    for key, value in count.items():
        if max_count == value:
            res.append(key)
    return res

"""
cookies1 = TreeNode(5, TreeNode(2), TreeNode(-3))
cookies2 = TreeNode(5, TreeNode(2), TreeNode(-5))

print(most_popular_cookie_combo(cookies1))  
print(most_popular_cookie_combo(cookies2))
"""

# Problem 4: Convert Binary Tree of Bakery Orders to Linked List
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def flatten_orders(orders):
    prev = None
    def preorder(node):
        nonlocal prev
        if not node:
            return
        left, right = node.left, node.right
        if prev:
            prev.right = node
            prev.left = None
        prev = node

        preorder(left)
        preorder(right)
    
    preorder(orders)
    return orders

"""
items = ["Croissant", "Cupcake", "Bagel", "Cake", "Pie", None, "Blondies"]
orders = build_tree(items)
print_tree(flatten_orders(orders))
"""

# Problem 5: Check Bakery Order Completeness
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def is_complete(root):
    if not root:
        return True
    q = deque()
    q.append(root)
    end = False

    while q:
        node = q.popleft()
        if node:
            if end:
                return False
            else:
                q.append(node.left)
                q.append(node.right)
        else:
            end = True
    return True

"""
items1 = ["Croissant", "Cupcake", "Bagel", "Cake", "Pie", "Blondies"]
order1 = build_tree(items1)
items2 = ["Croissant", "Cupcake", "Bagel", "Cake", "Pie", None, "Blondies"]
order2 = build_tree(items2)

print(is_complete(order1))
print(is_complete(order2))
"""

# Problem 6: Vertical Bakery Display
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def vertical_inventory_display(root):
    if not root:
        return
    table = collections.defaultdict(list)

    q = deque([(root, 0)])
    min_index, max_index = 0, 0
    while q:
        node, index = q.popleft()
        table[index].append(node.val)
        min_index = min(min_index, index)
        max_index = max(max_index, index)

        if node.left:
            q.append((node.left, index-1))
        if node.right:
            q.append((node.right, index+1))
    
    res = []
    for i in range(min_index, max_index + 1):
        res.append(table[i])
    return res

"""
inventory_items = ["Bread", "Croissant", "Donut", None, None, "Bagel", "Tart"]
inventory1 = build_tree(inventory_items)

print(vertical_inventory_display(inventory1))  

inventory_items = ["Bread", "Croissant", "Donut", "Muffin", "Scone", "Bagel", "Tart", None, None, "Pie", None, "Cake"]
inventory2 = build_tree(inventory_items)

print(vertical_inventory_display(inventory2))
"""  