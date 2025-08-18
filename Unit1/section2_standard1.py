# Problem 1: Reverse Sentence
def reverse_sentence(sentence):
    new_list = sentence.split(" ")
    new_list = new_list[::-1]
    return ' '.join(new_list)

"""
sentence = "tubby little cubby all stuffed with fluff"
print(reverse_sentence(sentence))

sentence = "Pooh"
print(reverse_sentence(sentence))
"""

# Problem 2: Goldilocks Number
def goldilocks_approved(nums):
    max_num = max(nums)
    min_num = min(nums)
    if len(nums) <= 2:
        return -1

    res = []
    for i in nums:
        if i != max_num and i != min_num:
            res.append(i)
    return min(res)

"""
nums = [3, 2, 1, 4]
print(goldilocks_approved(nums))

nums = [1, 2]
print(goldilocks_approved(nums))

nums = [2, 1, 3]
print(goldilocks_approved(nums))
"""

# Problem 3: Delete Minimum
def delete_minimum_elements(hunny_jar_sizes):
    new_list = []
    while hunny_jar_sizes:
        element = min(hunny_jar_sizes)
        new_list.append(element)
        hunny_jar_sizes.remove(element)
    return new_list

"""
hunny_jar_sizes = [5, 3, 2, 4, 1]
print(delete_minimum_elements(hunny_jar_sizes))

hunny_jar_sizes = [5, 2, 1, 8, 2]
print(delete_minimum_elements(hunny_jar_sizes))
"""

# Problem 4: Sum of Digits
def sum_of_digits(num):
    num = abs(num)
    total = 0
    while num > 0:
        reminder = num % 10
        num //= 10
        total += reminder     
    return total

"""
num = 423
print(sum_of_digits(num))

num = 4
print(sum_of_digits(num))
"""

