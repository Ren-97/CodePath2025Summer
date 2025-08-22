# Problem 1: Hundred Acre Wood
def welcome():
    print("Welcome to Hundred Acre Wood")

"""
welcome()
"""

# Problem 2: Greeting
def greeting(name):
    intro = welcome()
    print(f"{intro} {name}! My name is Ren.")

"""    
greeting('Alex')
"""

# Problem 3: Catchphrase
def print_catchphrase(character):
    if character == "Pooh":
        print("Oh bother!")
    elif character == "Tigger":
        print("TTFN: Ta-ta for now!")
    elif character == "Eeyore":
        print("Thanks for noticing me.")
    elif character == "Christopher Robin":
        print("Silly old bear.")
    else:
        print(f"Sorry! I don't know {character}'s catchphrase!")

"""     
character = "Pooh"
print_catchphrase(character)

character = "Piglet"
print_catchphrase(character)
"""  

# Problem 4: Return Item
def get_item(items, x):
    if x >= len(items):
        return None
    else:
        return items[x]

"""  
items = ["piglet", "pooh", "roo", "rabbit"]
x = 2
print(get_item(items, x))

items = ["piglet", "pooh", "roo", "rabbit"]
x = 5
print(get_item(items, x))
"""  

# Problem 5: Total Honey
def sum_honey(hunny_jars):
    if not hunny_jars:
        return 0
    total = 0
    for jar in hunny_jars:
        total += jar
    return total

"""
hunny_jars = [2, 3, 4, 5]
print(sum_honey(hunny_jars))

hunny_jars = []
print(sum_honey(hunny_jars))
"""

# Problem 6: Double Trouble
def doubled(hunny_jars):
    return [h * 2 for h in hunny_jars]

"""
hunny_jars = [1, 2, 3]
print(doubled(hunny_jars))
"""

# Problem 7: Poohsticks
def count_less_than(race_times, threshold):
    return sum([1 for time in race_times if time < threshold])

"""
race_times = [1, 2, 3, 4, 5, 6]
threshold = 4
print(count_less_than(race_times, threshold))

race_times = []
threshold = 4
print(count_less_than(race_times, threshold))
"""

# Problem 8: Pooh's To Do's
def print_todo_list(tasks):
    print("Pooh's To Dos:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

"""
task = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
print_todo_list(task)

task = []
print_todo_list(task)
"""

# Problem 9: Pairs
def can_pair(item_quantities):
    if not item_quantities:
        return True
    for num in item_quantities:
        if num % 2 == 1:
            return False
    return True

"""
item_quantities = [2, 4, 6, 8]
print(can_pair(item_quantities))

item_quantities = [1, 2, 3, 4]
print(can_pair(item_quantities))

item_quantities = []
print(can_pair(item_quantities))
"""

# Problem 10: Split Haycorns
import math

def split_haycorns(quantity):
    divisior = []
    sqrt_ = int(math.sqrt(quantity))
    for i in range(1, sqrt_+1):
        if quantity % i == 0:
            divisior.append(i)
            if quantity // i != i:
                divisior.append(quantity // i)
    return divisior

"""
quantity = 6
print(split_haycorns(quantity))

quantity = 1
print(split_haycorns(quantity))
"""

# Problem 11: T-I-Double Guh-ER
def tiggerfy(s):
    res = ""
    for letter in s:
        if letter.lower() not in "tiger":
            res += letter
    return res

"""
s = "suspicerous"
print(tiggerfy(s))

s = "Trigger"
print(tiggerfy(s))

s = "Hunny"
print(tiggerfy(s))
"""

# Problem 12: Thistle Hunt
def locate_thistles(items):
    res = []
    for i, item in enumerate(items):
        if item == "thistle":
            res.append(i)
    return res

"""
items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
print(locate_thistles(items))

items = ["book", "bouncy ball", "leaf", "red balloon"]
print(locate_thistles(items))
"""