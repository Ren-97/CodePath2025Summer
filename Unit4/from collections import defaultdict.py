from collections import defaultdict 
def count_material_usage(brands):
    dict_ = defaultdict(int)
    for b in brands:
        for mat in b["materials"]:
            dict_[mat] += 1
    return dict_

brands = [
    {"name": "EcoWear", "materials": ["organic cotton", "recycled polyester"]},
    {"name": "GreenThreads", "materials": ["organic cotton", "bamboo"]},
    {"name": "SustainableStyle", "materials": ["bamboo", "recycled polyester"]}
]

brands_2 = [
    {"name": "NatureWear", "materials": ["hemp", "linen"]},
    {"name": "Earthly", "materials": ["organic cotton", "hemp"]},
    {"name": "GreenFit", "materials": ["linen", "recycled wool"]}
]

brands_3 = [
    {"name": "OrganicThreads", "materials": ["organic cotton"]},
    {"name": "EcoFashion", "materials": ["recycled polyester", "hemp"]},
    {"name": "GreenLife", "materials": ["recycled polyester", "bamboo"]}
]

print(count_material_usage(brands))
print(count_material_usage(brands_2))
print(count_material_usage(brands_3))


def organize_fabrics(fabrics):
    fabrics_sorted = sorted(fabrics, key = lambda x:x[1], reverse = True)
    return [f[0] for f in fabrics_sorted]

fabrics = [("Organic Cotton", 8), ("Recycled Polyester", 6), ("Bamboo", 7), ("Hemp", 9)]
fabrics_2 = [("Linen", 5), ("Recycled Wool", 9), ("Tencel", 7), ("Organic Cotton", 6)]
fabrics_3 = [("Linen", 4), ("Hemp", 8), ("Recycled Polyester", 5), ("Bamboo", 7)]

print(organize_fabrics(fabrics))
print(organize_fabrics(fabrics_2))
print(organize_fabrics(fabrics_3))

def organize_fabric_rolls(fabric_rolls):
    pair = []
    sorted_fabric = sorted(fabric_rolls) #nlogn``
    n = len(sorted_fabric)
    i = 0
    while i < n-1:
        pair.append((sorted_fabric[i], sorted_fabric[i+1]))
        i += 2
    
    if n % 2 == 1:
        pair.append(sorted_fabric[-1])
        return pair
    else:
        return pair
    
fabric_rolls = [15, 10, 25, 30, 22]
fabric_rolls_2 = [5, 8, 10, 7, 12, 14]
fabric_rolls_3 = [40, 10, 25, 15, 30]

print(organize_fabric_rolls(fabric_rolls))
print(organize_fabric_rolls(fabric_rolls_2))
print(organize_fabric_rolls(fabric_rolls_3))