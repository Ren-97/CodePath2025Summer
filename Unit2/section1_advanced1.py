# Problem 1: Counting Treasure
def total_treasures(treasure_map):
    return sum(treasure_map.values())

""" 
treasure_map1 = {
    "Cove": 3,
    "Beach": 7,
    "Forest": 5
}

treasure_map2 = {
    "Shipwreck": 10,
    "Cave": 20,
    "Lagoon": 15,
    "Island Peak": 5
}

print(total_treasures(treasure_map1)) 
print(total_treasures(treasure_map2)) 
"""

# Problem 2: Pirate Message Check
def can_trust_message(message):
    new = set()
    for i in message:
        if i.isalpha():
            new.add(i)
    return len(new) == 26

"""
message1 = "sphinx of black quartz judge my vow"
message2 = "trust me"

print(can_trust_message(message1))
print(can_trust_message(message2))
"""

# Problem 3: Find All Duplicate Treasure Chests in an Array
import collections
def find_duplicate_chests(chests):
    count = collections.Counter(chests)
    duplicates = [num for num, freq in count.items() if freq == 2]
    return duplicates

"""
chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
chests2 = [1, 1, 2]
chests3 = [1]

print(find_duplicate_chests(chests1))
print(find_duplicate_chests(chests2))
print(find_duplicate_chests(chests3))
"""

# Problem 4: Booby Trap
def is_balanced(code):
    count = collections.Counter(code)
    freq = collections.Counter(count.values())
    if len(freq) == 1 or len(freq) > 2:
        return False
    
    (count1, freq1), (count2, freq2) = freq.items()
    if abs(count1 - count2) == 1:
        return True
    else:
        return False

"""
code1 = "arghh"
code2 = "haha"

print(is_balanced(code1)) 
print(is_balanced(code2)) 
"""

# Problem 5: Overflowing With Gold
def find_treasure_indices(gold_amounts, target):
    seen = {}
    for i, amount in enumerate(gold_amounts):
        rest = target - amount
        if rest in seen:
            return [seen[rest], i]
        seen[amount] = i

"""
gold_amounts1 = [2, 7, 11, 15]
target1 = 9

gold_amounts2 = [3, 2, 4]
target2 = 6

gold_amounts3 = [3, 3]
target3 = 6

print(find_treasure_indices(gold_amounts1, target1))  
print(find_treasure_indices(gold_amounts2, target2))  
print(find_treasure_indices(gold_amounts3, target3))
"""

# Problem 6: Organize the Pirate Crew
def organize_pirate_crew(group_sizes):
    pirate_sizes = collections.defaultdict(list)
    res = []
    for id, size in enumerate(group_sizes):
        pirate_sizes[size].append(id)
        if len(pirate_sizes[size]) == size:
            res.append(pirate_sizes[size])
            pirate_sizes[size] = []
    return res

"""
group_sizes1 = [3, 3, 3, 3, 3, 1, 3]
group_sizes2 = [2, 1, 3, 3, 3, 2]

print(organize_pirate_crew(group_sizes1))
print(organize_pirate_crew(group_sizes2)) 
"""

# Problem 7: Minimum Number of Steps to Match Treasure Maps
def min_steps_to_match_maps(map1, map2):
    count1 = collections.Counter(map1)
    count2 = collections.Counter(map2)
    res = 0
    for char in count1:
        if count1[char] > count2.get(char, 0):
            res += count1[char] - count2.get(char, 0)
    return res

"""
map1_1 = "bab"
map2_1 = "aba"
map1_2 = "treasure"
map2_2 = "huntgold"
map1_3 = "anagram"
map2_3 = "mangaar"

print(min_steps_to_match_maps(map1_1, map2_1))
print(min_steps_to_match_maps(map1_2, map2_2))
print(min_steps_to_match_maps(map1_3, map2_3))
"""

# Problem 8: Counting Pirates' Action Minutes
from collections import defaultdict
def counting_pirates_action_minutes(logs, k):
    ans = [0] * k
    dict_ = defaultdict(set)
    for id, min in logs:
        dict_[id].add(min)
    
    for id, min in dict_.items():
        n = len(min)
        if 1 <= n <= k:
            ans[n-1] += 1
    return ans

"""
logs1 = [[0, 5], [1, 2], [0, 2], [0, 5], [1, 3]]
k1 = 5
logs2 = [[1, 1], [2, 2], [2, 3]]
k2 = 4

print(counting_pirates_action_minutes(logs1, k1)) 
print(counting_pirates_action_minutes(logs2, k2))
"""
