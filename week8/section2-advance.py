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

# Problem 1: Sorting Plants by Rarity
def sort_plants(collection):
    res = []
    def inorder(node):
        if not node:
            return
        inorder(node.left)
        res.append((node.key, node.val))
        inorder(node.right)
    inorder(collection)
    return res

#values = [(3, "Monstera"), (1, "Pothos"), (5, "Witchcraft Orchid"), None, (2, "Spider Plant"), (4, "Hoya Motoskei")]
#collection = build_tree(values)

#print(sort_plants(collection))

# Problem 2: Flower Finding 
def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right
       
def find_flower(inventory, name):
    if not inventory:
        return False
    if inventory.val == name:
        return True
    elif inventory.val < name:
        return find_flower(inventory.right, name)
    else:
        return find_flower(inventory.left, name)
    
values = ["Rose", "Lily", "Tulip", "Daisy", "Lilac", None, "Violet"]
garden = build_tree(values)

#print(find_flower(garden, "Lilac"))  
#print(find_flower(garden, "Sunflower")) 

#Problem 3: Adding a New Plant to the Collection
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

def add_plant(collection, name):
    if not collection:
        return TreeNode(name)
    if collection.val < name:
        collection.right = add_plant(collection.right, name)
    else:
        collection.left = add_plant(collection.left, name)
    return collection
    
# Using build_tree() function at the top of page
#values = ["Money Tree", "Fiddle Leaf Fig", "Snake Plant"]
#collection = build_tree(values)

# Using print_tree() function at the top of page
#print_tree(add_plant(collection, "Aloe"))

#Problem 4: Remove Plant
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def remove_plant(collection, name):
    if not collection:
        return None
    if collection.val < name:
        collection.right = remove_plant(collection.right, name)
    elif collection.val > name:
        collection.left = remove_plant(collection.left, name)
    else:
        if collection.left is None:
            return collection.right
        elif collection.right is None:
            return collection.left
        else:
            predecessor = find_max(collection.left)
            collection.val = predecessor.val
            collection.left = remove_plant(collection.left, predecessor.val)
    return collection

def find_max(node):
    while node.right:
        node = node.right
    return node

# Using build_tree() function at the top of page
#values = ["Money Tree", "Hoya", "Pilea", None, "Ivy", "Orchid", "ZZ Plant"]
#collection = build_tree(values)

# Using print_tree() function at the top of page
#print_tree(remove_plant(collection, "Pilea"))

# Problem 5: Find Most Common Plants in Collection
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

import collections
def find_most_common(root):
    if not root:
        return []
    count = collections.defaultdict(int)

    def traverse(node):
        if node:
            count[node.val] += 1
            traverse(node.left)
            traverse(node.right)

    traverse(root)
    max_count = max(count.values())
    return [plant for plant, freq in count.items() if freq == max_count]

#values = ["Hoya", None, "Pothos", "Pothos"]
#collection1 = build_tree(values)
#print(find_most_common(collection1))
#values = ["Hoya", "Aloe", "Pothos", "Aloe", None, "Pothos"]
#collection2 = build_tree(values)
#print(find_most_common(collection2))

# Problem 6: Split Collection
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def split_collection(collection, target):
    if not collection:
        return None, None
    
    if collection.val == target:
        right_subtree = collection.right
        collection.right = None
        return collection, right_subtree
    elif collection.val < target:
        smaller_subtree, larger_subtree = split_collection(collection.right, target)
        collection.right = smaller_subtree
        return collection, larger_subtree
    else:
        smaller_subtree, larger_subtree = split_collection(collection.left, target)
        collection.left = larger_subtree
        return smaller_subtree, collection
    
#values = ["Money Tree", "Hoya", "Pilea", "Aloe", "Ivy", "Orchid", "ZZ Plant"]
#collection = build_tree(values)
#left, right = split_collection(collection, "Hoya")
#print_tree(left)
#print_tree(right)

# Problem 7: Pruning Pothos
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def prune(root, target):
    if not root:
        return None
    root.left = prune(root.left, target)
    root.right = prune(root.right, target)
    if not root.left and not root.right and root.val == target:
        return None
    return root


#values = ["Healthy", "Dying", "Healthy", "Dying", None, "Dying", "New Growth"]
#pothos1 = build_tree(values)
#print_tree(prune(pothos1, "Dying"))
#
#values = ["Healthy", "Aphids", "Aphids", "Aphids", "New Growth"]
#pothos2 = build_tree(values)
#print_tree(prune(pothos2, "Aphids"))
    
# Problem 8: Find the Lowest Common Ancestor in a Plant Tree Based on Species Names
class TreeNode():
    def __init__(self, species, parent=None, left=None, right=None):
        self.val = species
        self.parent = parent # Parent of node
        self.left = left
        self.right = right

def lca(root, p, q):
    if not root:
        return None
    if p == root.val or q == root.val:
        return root
    
    left = lca(root.left, p, q)
    right = lca(root.right, p, q)

    if left and right:
        return root
    else:
        return left or right
    
fern = TreeNode("fern")
cactus = TreeNode("cactus", fern)
rose = TreeNode("rose", fern)
bamboo = TreeNode("bamboo", cactus)
dahlia = TreeNode("dahlia", cactus)
lily = TreeNode("lily", rose)
oak = TreeNode("oak", rose)

fern.left, fern.right = cactus, rose
cactus.left, cactus.right = bamboo, dahlia
rose.left, rose.right = lily, oak

print(lca(fern, "cactus", "rose").val)
print(lca(fern, "bamboo", "oak").val)