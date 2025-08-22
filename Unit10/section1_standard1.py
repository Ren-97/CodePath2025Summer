# Problem 1: Graphing Flights
flights = {
    "JFK": ["LAX", "DFW"],
    "LAX": ["JFK"],
    "DFW": ["JFK", "ATL"],
    "ATL": ["DFW"]
}

"""
print(list(flights.keys()))
print(list(flights.values()))
print(flights["JFK"])
"""

# Problem 2: There and Back
def bidirectional_flights(flights):
    for i in range(len(flights)):
        for j in flights[i]:
            if i not in flights[j]:
                return False
    return True

"""
flights1 = [[1, 2], [0], [0, 3], [2]]
flights2 = [[1, 2], [], [0], [2]]

print(bidirectional_flights(flights1))
print(bidirectional_flights(flights2))
"""

# Problem 3: Finding Direct Flights
def get_direct_flights(flights, source):
    res = []
    for j in range(len(flights)):
        if flights[source][j] == 1:
            res.append(j)
    return res

"""
flights = [
            [0, 1, 1, 0],
            [1, 0, 0, 0],
            [1, 1, 0, 1],
            [0, 0, 0, 0]]

print(get_direct_flights(flights, 2))
print(get_direct_flights(flights, 3))
"""

# Problem 4: Converting Flight Representations
import collections
def get_adj_dict(flights):
    adj = collections.defaultdict(list)
    for u, v in flights:
        adj[u].append(v)
        adj[v].append(u)
    return adj

"""
flights = [['Cape Town', 'Addis Ababa'], ['Cairo', 'Lagos'], ['Lagos', 'Addis Ababa'], 
            ['Nairobi', 'Cairo'], ['Cairo', 'Cape Town']]
print(get_adj_dict(flights))
"""

# Problem 5: Find Center of Airport 
def find_center(terminals):
    degree = collections.defaultdict(int)
    nodes = set()
    for u, v in terminals:
        degree[u] += 1
        degree[v] += 1
        nodes.add(u)
        nodes.add(v)

    for node, deg in degree.items():
        if deg == len(nodes) - 1:
            return node
    return None

"""    
terminals1 = [[1,2],[2,3],[4,2]]
terminals2 = [[1,2],[5,1],[1,3],[1,4]]

print(find_center(terminals1))
print(find_center(terminals2))
"""

# Problem 6: Finding All Reachable Destinations
from collections import deque
def get_all_destinations1(flights, start):
    visited = set()
    q = deque([start])
    while q:
        u = q.popleft()
        for v in flights[u]:
            if v not in visited:
                visited.add(v)
                q.append(v)
    return list(visited)

"""
flights = {
    "Tokyo": ["Sydney"],
    "Sydney": ["Tokyo", "Beijing"],
    "Beijing": ["Mexico City", "Helsinki"],
    "Helsinki": ["Cairo", "New York"],
    "Cairo": ["Helsinki", "Reykjavik"],
    "Reykjavik": ["Cairo", "New York"],
    "Mexico City": ["Sydney"],
    "New York": []   
}

print(get_all_destinations1(flights, "Beijing"))
print(get_all_destinations1(flights, "Helsinki"))
"""

# Problem 7: Finding All Reachable Destinations II
def get_all_destinations2(flights, start):
    visited = set()
    result = []

    def dfs(u):
        for v in flights[u]:
            if v not in visited:
                visited.add(v)
                result.append(v)
                dfs(v)

    visited.add(start) 
    dfs(start)
    return result

"""
flights = {
    "Tokyo": ["Sydney"],
    "Sydney": ["Tokyo", "Beijing"],
    "Beijing": ["Mexico City", "Helsinki"],
    "Helsinki": ["Cairo", "New York"],
    "Cairo": ["Helsinki", "Reykjavik"],
    "Reykjavik": ["Cairo", "New York"],
    "Mexico City": ["Sydney"],
    "New York": []   
}

print(get_all_destinations2(flights, "Beijing"))
print(get_all_destinations2(flights, "Helsinki"))
"""


# Problem 8: Find Itinerary
def find_itinerary(boarding_passes):
    dict_ = {}
    for u, v in boarding_passes:
        dict_[u] = v

    visited = set()
    indegree_1 = set()
    for u, v in boarding_passes:
        visited.add(u)
        visited.add(v)
        indegree_1.add(v)
    start = visited - indegree_1
    start =  list(start)[0]

    res = [start]
    while start in dict_:
        start = dict_[start]
        res.append(start)
    return res

"""
boarding_passes_1 = [
                    ("JFK", "ATL"),
                    ("SFO", "JFK"),
                    ("ATL", "ORD"),
                    ("LAX", "SFO")]

boarding_passes_2 = [
                    ("LAX", "DXB"),
                    ("DFW", "JFK"),
                    ("LHR", "DFW"),
                    ("JFK", "LAX")]

print(find_itinerary(boarding_passes_1))
print(find_itinerary(boarding_passes_2))
"""