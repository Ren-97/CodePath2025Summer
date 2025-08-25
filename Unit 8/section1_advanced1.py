# Problem 1: Ivy Cutting
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def right_vine(root):
    if not root or not root.right:
        return [root.val]
    res = []
    cur = root
    while cur:
        res.append(cur.val)
        if cur.right:
            cur = cur.right
        else:
            break
    return res
# O(logn) time
# O(logn) space

"""
ivy1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))
ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

print(right_vine(ivy1))
print(right_vine(ivy2))
"""

# Problem 2: Ivy Cutting II
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def right_vine(root):
    if not root:
        return []
    
    if not root.right:
        return [root.val]
    else:
        return [root.val] + right_vine(root.right)
# O(logn) time
# O(logn) space

"""
ivy1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))
ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

print(right_vine(ivy1))
print(right_vine(ivy2))
"""

# Problem 3: Pruning Plans
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def survey_tree(root):
    res = []
    def dfs(node):
        if not node:
            return 
        dfs(node.left)
        dfs(node.right)
        res.append(node.val)
    dfs(root)
    return res
# O(n) time
# O(n) space

"""
magnolia = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                        TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

print(survey_tree(magnolia))
"""

# Problem 4: Sum Inventory
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

# BFS, iterative
from collections import deque
def sum_inventory(inventory):
    if not inventory:
        return 0
    q = deque()
    q.append(inventory)
    res = 0

    while q:
        for i in range(len(q)):
            node = q.popleft()
            res += node.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return res
# O(n) time
# O(n) space  

# DFS, iterative  
def sum_inventory(inventory):
    if not inventory:
        return 0
    stack = [inventory]
    res = 0

    while stack:
        cur = stack.pop()
        res += cur.val
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)
    return res
# O(n) time
# O(logn) space         

# DFS, recursive
def sum_inventory(inventory):
    if not inventory:
        return 0
    return inventory.val + sum_inventory(inventory.left) + sum_inventory(inventory.right)
# O(n) time
# O(logn) space

"""    
inventory = TreeNode(40, 
                    TreeNode(5, TreeNode(20)),
                            TreeNode(10, TreeNode(1), TreeNode(30)))

print(sum_inventory(inventory))
"""

# Problem 5: Calculating Yield II
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def calculate_yield(root):
    def dfs(node):
        if not node.left and not node.right:
            return node.val
        left = dfs(node.left)
        right = dfs(node.right)

        if node.val == "+":
            return left + right
        elif node.val == "-":
            return left - right
        elif node.val == "*":
            return left * right
        elif node.val == "/":
            return left / right

    return dfs(root)
# O(n) time
# O(logn) space
    
"""
root = TreeNode("+")
root.left = TreeNode("-")
root.right = TreeNode("*")
root.left.left = TreeNode(4)
root.left.right = TreeNode(2)
root.right.left = TreeNode(10)
root.right.right = TreeNode(2)

print(calculate_yield(root))
"""

# Problem 6: Plant Classifications
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def get_most_specific(taxonomy):
    if not taxonomy:
        return []
    res = []
    def dfs(node):
        if node.left:
            dfs(node.left)
        if node.right:
            dfs(node.right)
        
        if not node.left and not node.right:
            res.append(node.val)
    dfs(taxonomy)
    return res
# O(n) time
# O(n) space

"""
plant_taxonomy = TreeNode("Plantae", 
                          TreeNode("Non-flowering", TreeNode("Mosses"), TreeNode("Ferns")),
                                  TreeNode("Flowering", TreeNode("Gymnosperms"), 
                                          TreeNode("Angiosperms", TreeNode("Monocots"), TreeNode("Dicots"))))

print(get_most_specific(plant_taxonomy))
"""

# Problem 7: Count Old Growth Trees
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def count_old_growth(root, threshold):
    if not root:
        return 0
    count = 0
    def dfs(node):
        nonlocal count
        if not node:
            return
        if node.val > threshold:
            count += 1
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return count
# O(n) time
# O(logn) space

"""
forest = TreeNode(100, 
                  TreeNode(1200, TreeNode(20)),
                          TreeNode(1500, TreeNode(700), TreeNode(2600)))

print(count_old_growth(forest, 1000))
"""

# Problem 8: Twinning Trees
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def is_identical(root1, root2):
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    if root1.val == root2.val:
        return is_identical(root1.left, root2.left) and is_identical(root1.right, root2.right)
    else:
        return False
# O(n) time
# O(logn) space

"""
root1 = TreeNode(1, TreeNode(2), TreeNode(3))
root2 = TreeNode(1, TreeNode(2), TreeNode(3))
root3 = TreeNode(1, TreeNode(2))
root4 = TreeNode(1, None, TreeNode(2))

print(is_identical(root1, root2))
print(is_identical(root3, root4))
"""    