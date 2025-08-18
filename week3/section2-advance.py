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
    
print(blueprint_approval([3, 5, 2, 1, 4])) 
print(blueprint_approval([7, 4, 6, 2, 5])) 

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

print(build_skyscrapers([10, 5, 8, 3, 7, 2, 9])) 
print(build_skyscrapers([7, 3, 7, 3, 5, 1, 6]))  
print(build_skyscrapers([8, 6, 4, 7, 5, 3, 2])) 

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

print(max_corridor_area([1, 8, 6, 2, 5, 4, 8, 3, 7])) 
print(max_corridor_area([1, 1])) 

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

print(min_swaps("][][")) 
print(min_swaps("]]][[[")) 
print(min_swaps("[]"))  
print(min_swaps("[[[]]]"))

# Problem 5: Designing a Balanced Room
