from collections import deque

# Problem 1: Blueprint Approval Process
def blueprint_approval(blueprints):
    q = deque(blueprints)
    approved = []
    sorted_list = sorted(blueprints)

    i = 0
    while q:
        cur = q.popleft()
        if cur == sorted_list[i]:
            approved.append(cur)
            i += 1
        else:
            q.append(cur)

    return approved

""" 
print(blueprint_approval([3, 5, 2, 1, 4])) 
print(blueprint_approval([7, 4, 6, 2, 5])) 
"""

# Problem 2: Build the Tallest Skyscraper
def build_skyscrapers(floors):
    if not floors:
        return 0
    
    q = deque(floors)
    prev = float('inf')
    total = 1
    while q:
        cur = q.popleft()
        if prev >= cur:
            prev = cur
        else:
            total += 1
            prev = cur
    return total

"""
print(build_skyscrapers([10, 5, 8, 3, 7, 2, 9])) 
print(build_skyscrapers([7, 3, 7, 3, 5, 1, 6]))  
print(build_skyscrapers([8, 6, 4, 7, 5, 3, 2]))
""" 

# Problem 3: Dream Corridor Design
def max_corridor_area(segments):
    n = len(segments)
    left, right = 0, n-1
    res = 0
    while left < right:
        w = min(segments[left], segments[right])
        d = right - left
        res = max(res, w*d)
        if segments[left] >= segments[right]:
            right -= 1
        else:
            left += 1
    return res

"""
print(max_corridor_area([1, 8, 6, 2, 5, 4, 8, 3, 7])) 
print(max_corridor_area([1, 1]))
""" 

# Problem 4: Dream Building Layout
def min_swaps(s):
    balance, max_balance = 0,0
    for c in s:
        if c == "[":
            balance += 1
        elif c == "]":
            balance -= 1

        if balance < 0:
            max_balance = max(max_balance, -balance)
    return (max_balance + 1) // 2

"""
print(min_swaps("][][")) 
print(min_swaps("]]][[[")) 
print(min_swaps("[]"))  
print(min_swaps("[[[]]]"))
print(min_swaps1("]]]][[[["))
"""

def min_swaps1(s):
    swap = 0
    open = 0
    for c in s:
        if c == '[':
            open += 1
        elif c == ']':
            open -= 1
            if open < 0:
                swap += 1
                open = 1
    return swap

# Problem 5: Designing a Balanced Room
def make_balanced_room(s):
    stack = []
    for i, char in enumerate(s):
        if char == "(":
            stack.append(["(", i])
        elif char == ")":
            if stack and stack[-1][0] == "(":
                stack.pop()
            else:
                stack.append([")", i])
    
    index = [i for char, i in stack]
    res = ""
    for i, char in enumerate(s):
        if i not in index:
            res += char
    return res

"""
print(make_balanced_room("art(t(d)e)sign)")) 
print(make_balanced_room("d)e(s)ign")) 
print(make_balanced_room("))(("))
"""

# Problem 6: Time to Complete Each Dream Design
def time_to_complete_dream_designs(design_times):
    n = len(design_times)
    ans = [0] * n
    stack = []
    for i in range(n):
        while stack and design_times[stack[-1]] < design_times[i]:
            index = stack.pop()
            ans[index] = i - index
        stack.append(i)
    return ans

"""
print(time_to_complete_dream_designs([3, 4, 5, 2, 1, 6, 7, 3])) 
print(time_to_complete_dream_designs([2, 3, 1, 4]))  
print(time_to_complete_dream_designs([5, 5, 5, 5]))
"""

# Problem 7: Next Greater Element
def next_greater_dream(dreams):
    n = len(dreams)
    ans = [-1] * n
    stack = []
    for i in range(n * 2):
        index = i % n
        while stack and dreams[stack[-1]] < dreams[index]:
            prev_index = stack.pop()
            ans[prev_index] = dreams[index]
        
        if i < n:
            stack.append(i)
    return ans

"""
print(next_greater_dream([1, 2, 1])) 
print(next_greater_dream([1, 2, 3, 4, 3]))
""" 