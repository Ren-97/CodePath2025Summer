# Problem 1: Balanced Art Collection
import collections

def find_balanced_subsequence(art_pieces):
    count = collections.Counter(art_pieces)
    max_length = 0

    for val in count:
        if val + 1 in count:
            max_length = max(max_length, count[val] + count[val+1])
    return max_length       

"""
art_pieces1 = [1,3,2,2,5,2,3,7]
art_pieces2 = [1,2,3,4]
art_pieces3 = [1,1,1,1]

print(find_balanced_subsequence(art_pieces1))
print(find_balanced_subsequence(art_pieces2))
print(find_balanced_subsequence(art_pieces3))
"""

# Problem 2: Verifying Authenticity
def is_authentic_collection(art_pieces):
    n = len(art_pieces) - 1
    count = collections.Counter(art_pieces)
    if len(set(count.keys())) != n:
        return False

    for i in range(1,n):
        if count[i] != 1:
            return False
    if count[n] != 2:
        return False
    return True

"""
collection1 = [2, 1, 3]
collection2 = [1, 3, 3, 2]
collection3 = [1, 1]

print(is_authentic_collection(collection1))
print(is_authentic_collection(collection2))
print(is_authentic_collection(collection3))
"""

# Problem 3: Gallery Wall
def organize_exhibition(collection):
    count = collections.Counter(collection)
    max_freq = max(count.values())
    res = [[] for _ in range(max_freq)]
    
    row_index = 0
    for item, count in count.items():
        for _ in range(count):
            res[row_index].append(item)
            row_index = (row_index + 1) % max_freq
    return res

"""
collection1 = ["O'Keefe", "Kahlo", "Picasso", "O'Keefe", "Warhol", 
              "Kahlo", "O'Keefe"]
collection2 = ["Kusama", "Monet", "Ofili", "Banksy"]

print(organize_exhibition(collection1))
print(organize_exhibition(collection2))
"""

# Problem 4: Gallery Subdomain Traffic
def subdomain_visits(cpdomains):
    dict_ = collections.defaultdict(int)
    for element in cpdomains:
        number, address = element.split(' ')
        dict_[address] += int(number)

        new_list = address.split('.')
        for i in range(1, len(new_list)):
            item = '.'.join(new_list[i:])
            dict_[item] += int(number)

    ans = []
    for key, value in dict_.items():
        ans.append(' '.join([str(value), key]))

    return ans

"""
cpdomains1 = ["9001 modern.artmuseum.com"]
cpdomains2 = ["900 abstract.gallery.com", "50 impressionism.com", 
              "1 contemporary.gallery.com", "5 medieval.org"]

print(subdomain_visits(cpdomains1))
print(subdomain_visits(cpdomains2))
"""

# Problem 4: Gallery Subdomain Traffic
def subdomain_visits(cpdomains):
    domains = {}
    for name in cpdomains:
        splitted = name.split()
        views = int(splitted[0])
        alldomains = splitted[1].split('.')
        if len(alldomains) == 2:
            fulldomains = [alldomains[0] + '.' + alldomains[1], alldomains[1]]
        elif len(alldomains) == 3:
            fulldomains = [alldomains[0] + '.' + alldomains[1] + '.' + alldomains[2], 
                           alldomains[1] + '.' + alldomains[2], alldomains[2]]
        for subdomain in fulldomains:
            if subdomain not in domains.keys():
                domains[subdomain] = views
            else:
                domains[subdomain] += views
    cpsubdomains = []
    for domain, view in domains.items():
        cpsubdomains.append(str(view) + ' ' + domain)
    return cpsubdomains

"""
cpdomains1 = ["9001 modern.artmuseum.com"]
cpdomains2 = ["900 abstract.gallery.com", "50 impressionism.com", 
              "1 contemporary.gallery.com", "5 medieval.org"]

print(subdomain_visits(cpdomains1))
print(subdomain_visits(cpdomains2))
"""

# Problem 5: Beautiful Collection
def beauty_sum(collection):
    res = 0
    n = len(collection)
    for i in range(n):
        count = collections.defaultdict(int)
        for j in range(i,n):
            count[collection[j]] += 1
            freq = count.values()
            beauty = max(freq) - min(freq)
            res += beauty
    return res

"""
print(beauty_sum("aabcb")) 
print(beauty_sum("aabcbaa"))
"""

# Problem 6: Counting Divisible Collections in the Gallery
def count_divisible_collections(collection_sizes, k):
    subarray = set()
    n = len(collection_sizes)
    for i in range(n):
        total = 0
        for j in range(i,n):
            total += collection_sizes[j]
            if total % k == 0:
                subarray.add(tuple(collection_sizes[i:j+1]))
    return len(subarray)

nums1 = [4, 5, 0, -2, -3, 1]
k1 = 5
nums2 = [5]
k2 = 9

"""
print(count_divisible_collections(nums1, k1))  
print(count_divisible_collections(nums2, k2))  
"""