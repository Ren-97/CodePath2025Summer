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

# Problem 1: Croquembouche II
class Puff():
     def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right

def listify_design(design):
    if not design:
        return []
    res = []
    q = deque([design])
    while q:
        layer = []
        for i in range(len(q)):
            flavor = q.popleft()
            layer.append(flavor.val)
            if flavor.left:
                q.append(flavor.left)
            if flavor.right:
                q.append(flavor.right)
        res.append(layer)
    return res
# O(n) time
# O(n) space

"""  
croquembouche = Puff("Vanilla", 
                    Puff("Chocolate", Puff("Vanilla"), Puff("Matcha")), 
                    Puff("Strawberry"))
print(listify_design(croquembouche))
"""  

# Problem 2: Icing Cupcakes in Zigzag Order
class TreeNode():
     def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right

def zigzag_icing_order(cupcakes):
    if not cupcakes:
        return []
    res = []
    q = deque([cupcakes])
    sign = 1

    while q:
        level = []
        for _ in range(len(q)):
            flavor = q.popleft()
            level.append(flavor.val)
            if flavor.left:
                q.append(flavor.left)
            if flavor.right:
                q.append(flavor.right)
        if sign == 1:
            res.extend(level)
        else:
            res.extend(level[::-1])
        sign *= -1
    return res
# O(n) time
# O(n) space

"""
flavors = ["Chocolate", "Vanilla", "Lemon", "Strawberry", None, "Hazelnut", "Red Velvet"]
cupcakes = build_tree(flavors)

print(zigzag_icing_order(cupcakes))
"""

# Problem 3: Larger Order Tree
class TreeNode():
     def __init__(self, order_size, left=None, right=None):
        self.val = order_size
        self.left = left
        self.right = right

def larger_order_tree(orders):
    # Reverse In-order Traversal
    if not orders:
        return None
    total = 0

    def reverse_inorder(node):
        nonlocal total
        if not node:
            return 
        reverse_inorder(node.right)
        temp = node.val
        node.val += total
        total += temp
        reverse_inorder(node.left)
    
    reverse_inorder(orders)
    return orders
# O(n) time
# O(logn) space

"""
# using build_tree() function included at top of page
order_sizes = [4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]
orders = build_tree(order_sizes)

# using print_tree() function included at top of page
print_tree(larger_order_tree(orders))
"""

# Problem 4: Find Next Order to Fulfill Today
class TreeNode():
     def __init__(self, order, left=None, right=None):
        self.val = order
        self.left = left
        self.right = right

def larger_order_tree(order_tree, order):
    if not order_tree:
        return None
    q = deque([order_tree])
    found_target = False
    while q:
        for _ in range(len(q)):
            cur = q.popleft()
            if found_target:
                return cur
            if cur is order:
                found_target = True
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        if found_target:
            return None
    return None
# O(n) time
# O(n) space

"""
cupcakes = TreeNode("Cupcakes")
macaron = TreeNode("Macaron")
cookies = TreeNode("Cookies")
cake = TreeNode("Cake")
eclair = TreeNode("Eclair")
croissant = TreeNode("Croissant")

cupcakes.left, cupcakes.right = macaron, cookies
macaron.right = cake
cookies.left, cookies.right = eclair, croissant

next_order1 = larger_order_tree(cupcakes, cake)
next_order2 = larger_order_tree(cupcakes, cookies)
print(next_order1.val if next_order1 else None)
print(next_order2.val if next_order2 else None)
"""

# Problem 5: Add Row of Cupcakes to Display
class TreeNode():
    def __init__(self, sweetness, left=None, right=None):
        self.val = sweetness
        self.left = left
        self.right = right

def add_row(display, flavor, depth):
    if depth == 1:
        new_root = TreeNode(flavor)
        new_root.left = display
        return new_root
    
    q = deque([display])
    cur_depth = 1
    while q:
        if cur_depth == depth - 1:
            for node in q:
                left_sub = node.left
                right_sub = node.right
                node.left = TreeNode(flavor)
                node.right = TreeNode(flavor)
                node.left.left = left_sub
                node.right.right = right_sub
            break

        next_q = []
        for node in q:
            if node.left:
                next_q.append(node.left)
            if node.right:
                next_q.append(node.right)
        q = next_q
        cur_depth += 1
    return display
# O(n) time
# O(n) space

"""
# Using build_tree() function included at top of page
cupcake_flavors = ["Chocolate", "Vanilla", "Strawberry", None, None, "Chocolate", "Red Velvet"]
display = build_tree(cupcake_flavors)

# Using print_tree() function included at top of page
print_tree(add_row(display, "Mocha", 3))
"""

# Problem 6: Maximum Icing Difference
class TreeNode():
    def __init__(self, sweetness, left=None, right=None):
        self.val = sweetness
        self.left = left
        self.right = right

def max_icing_difference(root):
    def dfs(node, max_val, min_val):
        if not node:
            return max_val - min_val
        
        max_val = max(max_val, node.val)
        min_val = min(min_val, node.val)

        left = dfs(node.left, max_val, min_val)
        right = dfs(node.right, max_val, min_val)
        return max(left, right)
    return dfs(root, root.val, root.val)
# O(n) time
# O(nlogn) space

"""
sweetness_levels = [8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13]
display = build_tree(sweetness_levels)

print(max_icing_difference(display))
"""