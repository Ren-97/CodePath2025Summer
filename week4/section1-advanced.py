#Problem 1: Brand Filter
def filter_sustainable_brands(brands, criterion):
    res = []
    for brand in brands:
        for criteria in brand['criteria']:
            if criteria in criterion:
                res.append(brand["name"])
    return res
# O(n*m)
# O(n)
brands = [
    {"name": "EcoWear", "criteria": ["eco-friendly", "ethical labor"]},
    {"name": "FastFashion", "criteria": ["cheap materials", "fast production"]},
    {"name": "GreenThreads", "criteria": ["eco-friendly", "carbon-neutral"]},
    {"name": "TrendyStyle", "criteria": ["trendy designs"]}
]

brands_2 = [
    {"name": "Earthly", "criteria": ["ethical labor", "fair wages"]},
    {"name": "FastStyle", "criteria": ["mass production"]},
    {"name": "NatureWear", "criteria": ["eco-friendly"]},
    {"name": "GreenFit", "criteria": ["recycled materials", "eco-friendly"]}
]

brands_3 = [
    {"name": "OrganicThreads", "criteria": ["organic cotton", "fair trade"]},
    {"name": "GreenLife", "criteria": ["recycled materials", "carbon-neutral"]},
    {"name": "FastCloth", "criteria": ["cheap production"]}
]

print(filter_sustainable_brands(brands, "eco-friendly"))
print(filter_sustainable_brands(brands_2, "ethical labor"))
print(filter_sustainable_brands(brands_3, "carbon-neutral"))

# Problem 2: Eco-Friendly Materials
from collections import defaultdict 
def count_material_usage(brands):
    dict_ = defaultdict(int)
    for brand in brands:
        for material in brand['materials']:
            dict_[material] += 1
    return dict_
# O(n*m)
# O(k)

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

# Problem 3: Fashion Trends
def find_trending_materials(brands):
    dict_ = defaultdict(int)
    for brand in brands:
        for material in brand['materials']:
            dict_[material] += 1
    res = [mat for mat, freq in dict_.items() if freq > 1]
    return res
#O(m*n+k)
#O(k)

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

print(find_trending_materials(brands))
print(find_trending_materials(brands_2))
print(find_trending_materials(brands_3))

# Problem 4: Fabric Pairing
def find_best_fabric_pair(fabrics, budget):
    res = ()
    max_price = 0
    n = len(fabrics)
    for i in range(n):
        mat1, cost1 = fabrics[i]
        for j in range(i+1,n):
            mat2, cost2 = fabrics[j]
            total = cost1 + cost2
            if total == budget:
                return (mat1, mat2)
            elif total < budget and total > max_price:
                max_price = total
                res = (mat1, mat2)
    return res
# O(n^2)
# O(1)

fabrics = [("Organic Cotton", 30), ("Recycled Polyester", 20), ("Bamboo", 25), ("Hemp", 15)]
fabrics_2 = [("Linen", 50), ("Recycled Wool", 40), ("Tencel", 30), ("Organic Cotton", 60)]
fabrics_3 = [("Linen", 40), ("Hemp", 35), ("Recycled Polyester", 25), ("Bamboo", 20)]

print(find_best_fabric_pair(fabrics, 45))
print(find_best_fabric_pair(fabrics_2, 70))
print(find_best_fabric_pair(fabrics_3, 60))

# Problem 5: Fabric Stacks
def organize_fabrics(fabrics):
    sorted_fabrics = sorted(fabrics, key=lambda x:x[1], reverse=True)
    return [fabrics[0] for fabrics in sorted_fabrics]


fabrics = [("Organic Cotton", 8), ("Recycled Polyester", 6), ("Bamboo", 7), ("Hemp", 9)]
fabrics_2 = [("Linen", 5), ("Recycled Wool", 9), ("Tencel", 7), ("Organic Cotton", 6)]
fabrics_3 = [("Linen", 4), ("Hemp", 8), ("Recycled Polyester", 5), ("Bamboo", 7)]

print(organize_fabrics(fabrics))
print(organize_fabrics(fabrics_2))
print(organize_fabrics(fabrics_3))

# Problem 6: Supply Chain
def process_supplies(supplies):
    sorted_supplies = sorted(supplies, key=lambda x: -x[1])
    return [name for name, _ in sorted_supplies]

supplies = [("Organic Cotton", 3), ("Recycled Polyester", 2), ("Bamboo", 4), ("Hemp", 1)]
supplies_2 = [("Linen", 2), ("Recycled Wool", 5), ("Tencel", 3), ("Organic Cotton", 4)]
supplies_3 = [("Linen", 3), ("Hemp", 2), ("Recycled Polyester", 5), ("Bamboo", 1)]

print(process_supplies(supplies))
print(process_supplies(supplies_2))
print(process_supplies(supplies_3))

# Problem 7: Calculate Fabric Waste
def calculate_fabric_waste(items, fabric_rolls):