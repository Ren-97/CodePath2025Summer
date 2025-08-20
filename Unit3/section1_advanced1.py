# Problem 1: Arrange Guest Arrival Order
def arrange_guest_arrival_order(arrival_pattern):
    n = len(arrival_pattern)
    stack = []
    res = []

    for i in range(n + 1):
        stack.append(str(i + 1))
        if i == n or arrival_pattern[i] == "I":
            while stack:
                res.append(stack.pop())
    return "".join(res)

"""
print(arrange_guest_arrival_order("IIIDIDDD"))  
print(arrange_guest_arrival_order("DDD"))
"""

# Problem 2: Reveal Attendee List in Order
import collections
def reveal_attendee_list_in_order(attendees):
    attendees = sorted(attendees, reverse = True)
    q = collections.deque()
    for num in attendees:
        if q:
            q.appendleft(q.pop())
        q.appendleft(num)
    return q

"""
print(reveal_attendee_list_in_order([17,13,11,2,3,5,7])) 
print(reveal_attendee_list_in_order([1,1000]))
"""

# Problem 3: Arrange Event Attendees by Priority
def arrange_attendees_by_priority(attendees, priority):
    lower = [x for x in attendees if x < priority]
    equal = [x for x in attendees if x == priority]
    higher = [x for x in attendees if x > priority]
    return lower + equal + higher

"""
# Two pointer not qualify "The relative order of the attendees within each priority group (less than, equal to, greater than) must be preserved.""
def arrange_attendees_by_priority(attendees, priority):
    res = attendees
    left = 0
    right = len(attendees) - 1
    i = 0
    while i <= right:
        if res[i] < priority:
            res[i], res[left] = res[left], res[i]
            i += 1
            left += 1
        elif res[i] > priority:
            res[i], res[right] = res[right], res[i]
            right -= 1
        else:
            i += 1
    return res

print(arrange_attendees_by_priority([9,12,5,10,14,3,10], 10)) 
print(arrange_attendees_by_priority([-3,4,3,2], 2)) 
"""

# Problem 4: Rearrange Guests by Attendance and Absence
def rearrange_guests(guests):
    pos_index = 0
    neg_index = 1
    res = [0] * len(guests)

    for i in range(len(guests)):
        if guests[i] < 0:
            res[neg_index] = guests[i]
            neg_index += 2
        else:
            res[pos_index] = guests[i]
            pos_index += 2
    return res

# Rearrange guests in-place without using extra space.
def rearrange_guests(guests):
    pos_ptr = 0 
    neg_ptr = 1
    n = len(guests) 
    
    while pos_ptr < n and neg_ptr < n:
        if guests[pos_ptr] > 0:
            pos_ptr += 2
        elif guests[neg_ptr] < 0:
            neg_ptr += 2
        else:
            guests[pos_ptr], guests[neg_ptr] = guests[neg_ptr], guests[pos_ptr]
            pos_ptr += 2
            neg_ptr += 2
    
    return guests

"""
print(rearrange_guests([3,1,-2,-5,2,-4]))  
print(rearrange_guests([-1,1]))
"""

# Problem 5: Minimum Changes to Make Schedule Balanced
def min_changes_to_make_balanced(schedule):
    stack = []
    for str in schedule:
        if stack and str == ")":
            if stack[-1] == "(":
                stack.pop()
            else:
                stack.append(str)
        else:
            stack.append(str)
    return len(stack)

"""
print(min_changes_to_make_balanced("())"))
print(min_changes_to_make_balanced("(((")) 
"""

"""
# Problem 6: Marking the Event Timeline
def mark_event_timeline(event, timeline):

    
print(mark_event_timeline("abc", "ababc"))     # Output: [0, 2]
print(mark_event_timeline("abca", "aabcaca"))  # Output: [3, 0, 1]
"""
