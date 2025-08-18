#def count_suits_iterative(suits):
#     count = 0
#     for suit in suits:
#         count+=1
#     return count

# def count_suits_recursive(suits):
#     if suits == []:
#         return 0
#     return 1 + count_suits_recursive(suits[1:]) if

# print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
# print(count_suits_recursive(["Mark I", "Mark I", "Mark III", "Mark IV"]))

# def sum_stones(stones):
#     if stones == []:
#         return 0
#     return stones[0] + sum_stones(stones[1:])


# print(sum_stones([5, 10, 15, 20, 25, 30]))
# print(sum_stones([12, 8, 22, 16, 10]))

# def count_suits_iterative(suits):
#     set_ = set()
#     for suit in suits:
#         set_.add(suit)
#     return len(set_)

# def count_suits_recursive(suits):
#     def helper(suits, set_):
#         if suits == []:
#             return len(set_)
#         set_.add(suits[0])
#         return helper(suits[1:], set_)
#     return helper(suits, set())


# print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
# print(count_suits_recursive(["Mark I", "Mark I", "Mark III"]))


# def fibonacci_growth(n):
#     if n <= 1:
#         return n
#     return fibonacci_growth(n-1) + fibonacci_growth(n-2)

# print(fibonacci_growth(5))
# print(fibonacci_growth(8))

# def power_of_four(n):
#     if n == 0:
#         return 1

#     if n > 0:
#         return 4 * power_of_four(n-1)
#     # else:
#     #     return 1 / (power_of_four(-n))
#     if n < 0:
#         return 1 / 4 * power_of_four(n+1)

# print(power_of_four(2))
# print(power_of_four(-2))

# power_of_four(-2) = 1 / power_of_four(2)


# def strongest_avenger(strengths):
#     def helper(strengths, max):
#         if strengths == []:
#             return max
#         if strengths[0] > max:
#             max = strengths[0]
#         return helper(strengths[1:], max)
#     return helper(strengths, float("-inf"))


# def strongest_avenger(strengths):
#     if len(strengths) == 1:
#         return strengths[0]
#     rest_max = strongest_avenger(strengths[1:])
#     if strengths[0] > rest_max:
#         return strengths[0]
#     else:
#         return rest_max

# print(strongest_avenger([88, 92, 95, 99, 97, 100, 94]))
# print(strongest_avenger([50, 75]))


def count_deposits(resources):
    if len(resources) == 0:
        return 0
    if resources[0] == "V":
        return 1 + count_deposits(resources[1:])
    else:
        return count_deposits(resources[1:]) 


print(count_deposits("VVVVV"))
print(count_deposits("VXVYGA"))
