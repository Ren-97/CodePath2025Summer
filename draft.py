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
    def __init__(self, val, key, left=None, right=None):
        self.key = key      # Plant price
        self.val = val      # Plant name
        self.left = left
        self.right = right

#We can define an array
#We can define a helper function that does inorder traversall, using recurssion
    #We need to check the base case of reaching a leaf node
    #Left -> Current -> Right
    #We need to append the value to our array, left, current, right
#Return the array

def sort_plants(collection):
    result = []

    #Base case
    def inorder(node):
        if not node:
            return
        inorder(node.left)
        result.append((node.key, node.val))
        inorder(node.right)
        
    inorder(collection)
    return result

#values = [(3, "Monstera"), (1, "Pothos"), (5, "Witchcraft Orchid"), None, (2, "Spider Plant"), (4, "Hoya Motoskei")]
#collection = build_tree(values)
#print(sort_plants(collection))

# Problem 2: Flower Finding

class TreeNode():
     def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right
        
def find_flower(inventory, name):
    # if not inventory:
    #     return False
    current = inventory
    while current: 
        if current.val == name:
            return True
        elif current.val > name:
            current = current.left
        else:
            current = current.right
    return False

values = ["Rose", "Lilac", "Tulip", "Daisy", "Lily" , None, "Violet"]
garden = build_tree(values)

print(find_flower(garden, "Lilac")) 
print(find_flower(garden, "Sunflower")) 

# Problem 3: Adding a New Plant to the Collection
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
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def add_plant(collection, name):
        # starting with current node
        # compare if it's less than or equal
        # if less; traverse left; otherwise right
        # base: once we're at the end, set it to left or right

        if collection is None:
            return TreeNode(name)

        if name < collection.val:
            collection.left = add_plant(collection.left, name)
        else:
            collection.right = add_plant(collection.right, name)

        return collection

# Time: O(logn)
# Space: 
# - Best: O(log n) - Depth of recursion(function call stack)

#values = ["Money Tree", "Fiddle Leaf Fig", "Snake Plant"]
#collection = build_tree(values)
#
## Using print_tree() function at the top of page
#print_tree(add_plant(collection, "Aloe"))

def remove_plant(collection, name):
    if not collection:
        return None
    if name < collection.val:
        collection.left = remove_plant(collection.left, name)
    elif name > collection.val:
        collection.right = remove_plant(collection.right, name)
    else:
        if not collection.left:
            return collection.right
        elif not collection.right:
            return collection.left
        else:
            predecessor = find(collection.left)
            collection.val = predecessor.val
            collection.left = remove_plant(collection.left, predecessor.val)
    return collection
def find(node):
    while node.right:
        node = node.right
    return node

# Using build_tree() function at the top of page
values = ["Money Tree", "Hoya", "Pilea", None, "Ivy", "Orchid", "ZZ Plant"]
collection = build_tree(values)

# Using print_tree() function at the top of page
print_tree(remove_plant(collection, "Pilea"))


def find_most_common(root):
    pass


# Breakout 42
# Angelyn Domingo, Amanuel Yilma, Divyansh Gupta, Ren Huang
# Let's connect on slack :DDD, thanks for all the help