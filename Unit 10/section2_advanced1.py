# Problem 1: Get Flight Cost
import heapq

# Dijkstra's algorithm
def calculate_cost(flights, start, dest):
    if start == dest:
        return 0
    if start not in flights:
        return -1
    
    pq = [(0, start)]
    min_cost = {start:0}

    while pq:
        cur_cost, cur_loc = heapq.heappop(pq)
        if cur_loc == dest:
            return cur_cost
        if cur_cost > min_cost.get(cur_loc, float('inf')):
            continue

        for next_loc, next_cost in flights[cur_loc]:
            new_cost = cur_cost + next_cost

            if new_cost < min_cost.get(next_loc, float('inf')):
                min_cost[next_loc] = new_cost
                heapq.heappush(pq, (new_cost, next_loc))
    return -1

"""
flights = {
    'LAX': [('SFO', 50)],
    'SFO': [('LAX', 50), ('ORD', 100), ('ERW', 210)],
    'ERW': [('SFO', 210), ('ORD', 100)],
    'ORD': [('ERW', 300), ('SFO', 100), ('MIA', 400)],
    'MIA': [('ORD', 400)]
}

print(calculate_cost(flights, 'LAX', 'MIA'))
"""

# Problem 2: Expanding Flight Offerings
def min_flights_to_expand(flights):
    visited = set()
    components = 0

    def dfs(node):
        visited.add(node)
        for nei in flights[node]:
            if nei not in visited:
                dfs(nei)
    
    for airpot in flights:
        if airpot not in visited:
            dfs(airpot)
            components += 1
    
    return components - 1

"""
flights = {
    'JFK': ['LAX', 'SFO'],
    'LAX': ['JFK', 'SFO'],
    'SFO': ['JFK', 'LAX'],
    'ORD': ['ATL'],
    'ATL': ['ORD']
}

print(min_flights_to_expand(flights))
"""

# Problem 3: Get Flight Itinerary
from collections import deque
def get_itinerary(flights, source, dest):
    q = deque([(source, [source])])
    visited = set()

    while q:
        src, path = q.popleft()
        if src == dest:
            return path
        if src not in visited:
            visited.add(src)
        else:
            continue

        for nei in flights[src]:
            q.append((nei, path + [nei]))
    return []

"""
flights = {
    'LAX': ['SFO'],
    'SFO': ['LAX', 'ORD', 'ERW'],
    'ERW': ['SFO', 'ORD'],
    'ORD': ['ERW', 'SFO', 'MIA'],
    'MIA': ['ORD']
}

print(get_itinerary(flights, 'LAX', 'MIA'))
"""

# Problem 4: Pilot Training
from collections import defaultdict
def can_complete_flight_training(num_courses, flight_prerequisites):
    graph = defaultdict(list)
    indegree = defaultdict(int)
    course = set()
    
    for a, b in flight_prerequisites:
        graph[b].append(a)
        indegree[a] += 1
        course.add(a)
        course.add(b)

    for c in course:
        indegree.setdefault(c, 0)
    
    q = deque()
    count = 0
    for c in indegree:
        if indegree[c] == 0:
            q.append(c)
    
    while q:
        c = q.popleft()
        count += 1
        for nei in graph[c]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)
    return count == num_courses

"""
flight_prerequisites_1 = [['Advanced Maneuvers', 'Basic Navigation']]
flight_prerequisites_2 = [['Advanced Maneuvers', 'Basic Navigation'], ['Basic Navigation', 'Advanced Maneuvers']]

print(can_complete_flight_training(2, flight_prerequisites_1))
print(can_complete_flight_training(2, flight_prerequisites_2))
"""

# Problem 5: Reorient Flight Routes
def min_reorient_flight_routes(n, connections):


n = 6
connections = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]

print(min_reorient_flight_routes(n, connections))