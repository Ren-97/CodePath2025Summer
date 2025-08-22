# Problem 1: Finding the Perfect Cruise
def find_cruise_length(cruise_lengths, vacation_length):
    left, right = 0, len(cruise_lengths) - 1
    while left <= right:
        mid = (left + right) // 2
        if cruise_lengths[mid] == vacation_length:
            return True
        elif cruise_lengths[mid] > vacation_length:
            right = mid - 1
        else:
            left = mid + 1
    return False

"""
print(find_cruise_length([9, 10, 11, 12, 13, 14, 15], 13))
print(find_cruise_length([8, 9, 12, 13, 13, 14, 15], 11))
"""

# Problem 2: Booking the Perfect Cruise Cabin
def find_cabin_index(cabins, preferred_deck):
    def binary_search(left, right):
        if left > right:
            return left
        mid = (left+right) // 2
        if cabins[mid] == preferred_deck:
            return mid
        elif cabins[mid] > preferred_deck:
            return binary_search(left, mid-1)
        else:
            return binary_search(mid+1, right)
    return binary_search(0, len(cabins) -1)

"""
print(find_cabin_index([1, 3, 5, 6], 5))
print(find_cabin_index([1, 3, 5, 6], 2))
print(find_cabin_index([1, 3, 5, 6], 7))
"""

# Problem 3: Count Checked In Passengers
def count_checked_in_passengers(rooms):
    left, right = 0, len(rooms) - 1
    first_one_index = len(rooms)
    while left <= right:
        mid = (left+right)//2
        if rooms[mid] == 1:
            first_one_index = mid
            right = mid - 1
        else:
            left = mid + 1
    return len(rooms) - first_one_index

"""
rooms1 = [0, 0, 0, 1, 1, 1, 1]
rooms2 = [0, 0, 0, 0, 0, 1]
rooms3 = [0, 0, 0, 0, 0, 0]

print(count_checked_in_passengers(rooms1)) 
print(count_checked_in_passengers(rooms2))
print(count_checked_in_passengers(rooms3))
"""

# Problem 4: Determining Profitability of Excursions
def is_profitable(excursion_counts):
    n = len(excursion_counts)
    left, right = 0, n
    while left <= right:
        mid = (left + right) // 2
        count = 0
        for i in range(n-1, -1, -1):
            if excursion_counts[i] >= mid:
                count += 1
            else:
                break
        if count == mid:
            return count
        elif count > mid:
            left = mid + 1
        else:
            right = mid - 1
    return -1

"""
print(is_profitable([3, 5]))
print(is_profitable([0, 0]))
print(is_profitable([5,5,5,5,5]))
"""

# Problem 5: Finding the Shallowest Point
def find_shallowest_point(arr):
    if len(arr) == 1:
        return arr[0]
    rest_min = find_shallowest_point(arr[1:])

    if arr[0] < rest_min:
        return arr[0]
    else:
        return rest_min

"""    
print(find_shallowest_point([5, 7, 2, 8, 3]))
print(find_shallowest_point([12, 15, 10, 21]))
"""

# Problem 6: Cruise Ship Treasure Hunt
def find_treasure(matrix, treasure):
    m, n = len(matrix), len(matrix[0])
    i, j = 0, n - 1
    while i < m and j > 0:
        if matrix[i][j] == treasure:
            return (i,j)
        elif matrix[i][j] <  treasure:
            i += 1  
        else:
            j -= 1
    return (-1, -1)

"""
rooms = [
    [1, 4, 7, 11],
    [8, 9, 10, 20],
    [11, 12, 17, 30],
    [18, 21, 23, 40]
]

print(find_treasure(rooms, 17))
print(find_treasure(rooms, 5))
"""