def find_cruise_length(cruise_lengths, vacation_length):
    left, right = 0, len(cruise_lengths) - 1
    while left <= right:
        mid = (left + right) // 2
        if cruise_lengths[mid] == vacation_length:
            return True
        elif cruise_lengths[mid] < vacation_length:
            left = mid + 1
        else:
            right = mid - 1
    return False

#print(find_cruise_length([9, 10, 11, 12, 13, 14, 15], 13))
#print(find_cruise_length([8, 9, 12, 13, 13, 14, 15], 11))


def find_cabin_index(cabins, preferred_deck):
    def find_mid(left, right):
        if left > right:
            return left
        mid = (left + right) // 2
        if cabins[mid] == preferred_deck:
            return mid
        elif cabins[mid] < preferred_deck:
            return find_mid(mid + 1, right)
        else:
            return find_mid(left, mid - 1)
    return find_mid(0, len(cabins) - 1)

#print(find_cabin_index([1, 3, 5, 6], 5))
#print(find_cabin_index([1, 3, 5, 6], 2))
#print(find_cabin_index([1, 3, 5, 6], 7))

def count_checked_in_passengers(rooms):
    # find the first 1's index
    if rooms[-1] == 0:
       return 0
    
    first_one_index = len(rooms)
    left, right = 0, len(rooms) - 1
    while left <= right:
        mid = (left + right) // 2
        if rooms[mid] == 1:
            first_one_index = mid
            right = mid - 1
        else:
            left = mid + 1
    return len(rooms) - first_one_index

rooms1 = [0, 0, 1, 1, 1]
rooms2 = [0, 0, 0, 0, 0, 1]
rooms3 = [0, 0, 0, 0, 0, 0]

#print(count_checked_in_passengers(rooms1)) 
#print(count_checked_in_passengers(rooms2))
#print(count_checked_in_passengers(rooms3))

def is_profitable(excursion_counts):
    left, right = 0, len(excursion_counts)-1
    while left <= right:
        mid = (left + right) // 2
        count = 0
        for i in range(len(excursion_counts)-1, -1, -1):
            if excursion_counts[i] >= mid:
                count += 1
            else:
                break
        if mid == count:
            return mid
        elif mid < count:
            left = mid + 1
        else:
            right = mid - 1
    return -1

print(is_profitable([3, 5]))
print(is_profitable([0, 0]))
print(is_profitable([5, 5,5,5,5]))

def find_shallowest_point(arr):
    if len(arr) == 1:
        return arr[0]
    rest_min = find_shallowest_point(arr[1:])

    if arr[0] < rest_min:
        return arr[0]
    else:
        return rest_min
    
print(find_shallowest_point([5, 7, 2, 8, 3]))
print(find_shallowest_point([12, 15, 10, 21]))



