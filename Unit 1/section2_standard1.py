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

# Problem 5: Bouncy, Flouncy, Trouncy, Pouncy
def final_value_after_operations(operations):
    tigger = 1
    for operation in operations:
        if operation in ["bouncy", "flouncy"]:
            tigger += 1
        elif operation in ["trouncy", "pouncy"]:
            tigger -= 1
    return tigger

"""
operations = ["trouncy", "flouncy", "flouncy"]
print(final_value_after_operations(operations))

operations = ["bouncy", "bouncy", "flouncy"]
print(final_value_after_operations(operations))
"""

# Problem 6: Acronym
def is_acronym(words, s):
    acronym = ""
    for word in words:
        acronym += word[0]
    return acronym == s

"""
words = ["christopher", "robin", "milne"]
s = "crm"
print(is_acronym(words, s)) 
"""

# Problem 7: Good Things Come in Threes
def make_divisible_by_3(nums):
    res = 0
    for num in nums:
        if num % 3 != 0:
            res += 1
    return res

"""
nums = [1, 2, 3, 4]
print(make_divisible_by_3(nums))

nums = [3, 6, 9]
print(make_divisible_by_3(nums))
"""

# Problem 8: Exclusive Elements
def exclusive_elemts(lst1, lst2):
    return list(set(lst1) ^ set(lst2))

"""
lst1 = ["pooh", "roo", "piglet"]
lst2 = ["piglet", "eeyore", "owl"]
print(exclusive_elemts(lst1, lst2))

lst1 = ["pooh", "roo"]
lst2 = ["piglet", "eeyore", "owl", "kanga"]
print(exclusive_elemts(lst1, lst2))

lst1 = ["pooh", "roo", "piglet"]
lst2 = ["pooh", "roo", "piglet"]
print(exclusive_elemts(lst1, lst2))
"""

# Problem 9: Merge Strings Alternately
def merge_alternately(word1, word2):
    res = "" 
    i = 0
    while i < len(word1) and i < len(word2):
        res += word1[i] + word2[i]
        i += 1
    
    if i < len(word1):
        res += word1[i:]
    if i < len(word2):
        res += word2[i:]
    return res

"""
word1 = "wol"
word2 = "oze"
print(merge_alternately(word1, word2))

word1 = "hfa"
word2 = "eflump"
print(merge_alternately(word1, word2))

word1 = "eyre"
word2 = "eo"
print(merge_alternately(word1, word2))
"""

# Problem 10: Eeyore's House
def good_pairs(pile1, pile2, k):
    res = 0
    for i in pile1:
        for j in pile2:
            if i < j * k:
                continue
            elif i % (j * k) == 0:
                res += 1
    return res

"""
pile1 = [1, 3, 4]
pile2 = [1, 3, 4]
k = 1
print(good_pairs(pile1, pile2, k))

pile1 = [1, 2, 4, 12]
pile2 = [2, 4]
k = 3
print(good_pairs(pile1, pile2, k))
"""