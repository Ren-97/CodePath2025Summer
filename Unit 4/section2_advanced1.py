# Problem 1: Count Unique Characters in a Script
def count_unique_characters(script):
    return len(set(script.keys()))
# O(n) time
# O(n) space

"""
script = {
    "Alice": ["Hello there!", "How are you?"],
    "Bob": ["Hi Alice!", "I'm good, thanks!"],
    "Charlie": ["What's up?"]
}
print(count_unique_characters(script)) 

script_with_redundant_keys = {
    "Alice": ["Hello there!"],
    "Alice": ["How are you?"],
    "Bob": ["Hi Alice!"]
}
print(count_unique_characters(script_with_redundant_keys))
"""

# Problem 2: Find Most Frequent Keywords
from collections import defaultdict
def find_most_frequent_keywords(scenes):
    count = defaultdict(int)
    for key, values in scenes.items():
        for word in values:
            count[word] += 1
    most_freq = max(count.values())
    return [key for key, value in count.items() if value == most_freq]
# O(n+m) time
# O(m) space

"""
scenes = {
    "Scene 1": ["action", "hero", "battle"],
    "Scene 2": ["hero", "action", "quest"],
    "Scene 3": ["battle", "strategy", "hero"],
    "Scene 4": ["action", "strategy"]
}
print(find_most_frequent_keywords(scenes))

scenes = {
    "Scene A": ["love", "drama"],
    "Scene B": ["drama", "love"],
    "Scene C": ["comedy", "love"],
    "Scene D": ["comedy", "drama"]
}
print(find_most_frequent_keywords(scenes))
"""

# Problem 3: Track Scene Transitions
def track_scene_transitions(scenes):
    for i in range(len(scenes) - 1):
        print(f"Transition from {scenes[i]} to {scenes[i+1]}")
# O(n) time
# O(1) space

"""
scenes = ["Opening", "Rising Action", "Climax", "Falling Action", "Resolution"]
track_scene_transitions(scenes)

scenes = ["Introduction", "Conflict", "Climax", "Denouement"]
track_scene_transitions(scenes)
"""

# Problem 4: Organize Scene Data by Date
def organize_scene_data_by_date(scene_records):
    return sorted(scene_records, key = lambda x: x[0])
# O(nlogn) time
# O(n) space using sorted bc it creates a new list
# O(1) space using sort bc it modifies original list

"""
scene_records = [
    ("2024-08-15", "Climax"),
    ("2024-08-10", "Introduction"),
    ("2024-08-20", "Resolution"),
    ("2024-08-12", "Rising Action")
]
print(organize_scene_data_by_date(scene_records))

scene_records = [
    ("2023-07-05", "Opening"),
    ("2023-07-07", "Conflict"),
    ("2023-07-01", "Setup"),
    ("2023-07-10", "Climax")
]
print(organize_scene_data_by_date(scene_records))
"""

# Problem 5: Filter Scenes by Keyword
def filter_scenes_by_keyword(scenes, keyword):
    res = []
    for scene in scenes:
        if keyword not in scene:
            res.append(scene)
    return res
# O(n) time
# O(n) space

"""
scenes = [
    "The hero enters the dark forest.",
    "A mysterious figure appears.",
    "The hero finds a hidden treasure.",
    "An eerie silence fills the air."
]
keyword = "hero"

filtered_scenes = filter_scenes_by_keyword(scenes, keyword)
print(filtered_scenes)

scenes = [
    "The spaceship lands on an alien planet.",
    "A strange creature approaches the crew.",
    "The crew prepares to explore the new world."
]
keyword = "crew"

filtered_scenes = filter_scenes_by_keyword(scenes, keyword)
print(filtered_scenes)
"""

# Problem 6: Manage Character Arcs
def manage_character_arc(events):
    stack = []
    for event in events:
        stack.append(event)
    return stack
# O(n) time
# O(n) space

"""
events = [
    "Character is introduced.",
    "Character faces a dilemma.",
    "Character makes a decision.",
    "Character grows stronger.",
    "Character achieves goal."
]

processed_arc = manage_character_arc(events)
print(processed_arc)

events = [
    "Character enters a new world.",
    "Character struggles to adapt.",
    "Character finds a mentor.",
    "Character gains new skills.",
    "Character faces a major setback.",
    "Character overcomes the setback."
]

processed_arc = manage_character_arc(events)
print(processed_arc)
"""

# Problem 7: Identify Repeated Themes
def identify_repeated_themes(scenes):
    count = defaultdict(int)
    for scene in scenes:
        count[scene["theme"]] += 1
    return [key for key, value in count.items() if value > 1]
# O(n) time
# O(n) space

"""
scenes = [
    {"scene": "The hero enters the dark forest.", "theme": "courage"},
    {"scene": "A mysterious figure appears.", "theme": "mystery"},
    {"scene": "The hero faces his fears.", "theme": "courage"},
    {"scene": "An eerie silence fills the air.", "theme": "mystery"},
    {"scene": "The hero finds a hidden treasure.", "theme": "discovery"}
]

repeated_themes = identify_repeated_themes(scenes)
print(repeated_themes)

scenes = [
    {"scene": "The spaceship lands on an alien planet.", "theme": "exploration"},
    {"scene": "A strange creature approaches.", "theme": "danger"},
    {"scene": "The crew explores the new world.", "theme": "exploration"},
    {"scene": "The crew encounters hostile forces.", "theme": "conflict"},
    {"scene": "The crew makes a narrow escape.", "theme": "danger"}
]

repeated_themes = identify_repeated_themes(scenes)
print(repeated_themes)
"""

# Problem 8: Analyze Storyline Continuity
def analyze_storyline_continuity(scenes):
    for i in range(len(scenes) - 1):
        if scenes[i]["timestamp"] > scenes[i+1]["timestamp"]:
            return False
    return True
# O(n) time
# O(1) space

"""
scenes = [
    {"scene": "The hero enters the dark forest.", "timestamp": 1},
    {"scene": "A mysterious figure appears.", "timestamp": 2},
    {"scene": "The hero faces his fears.", "timestamp": 3},
    {"scene": "The hero finds a hidden treasure.", "timestamp": 4},
    {"scene": "An eerie silence fills the air.", "timestamp": 5}
]

continuity = analyze_storyline_continuity(scenes)
print(continuity)

scenes = [
    {"scene": "The spaceship lands on an alien planet.", "timestamp": 3},
    {"scene": "A strange creature approaches.", "timestamp": 2},
    {"scene": "The crew explores the new world.", "timestamp": 4},
    {"scene": "The crew encounters hostile forces.", "timestamp": 5},
    {"scene": "The crew makes a narrow escape.", "timestamp": 6}
]

continuity = analyze_storyline_continuity(scenes)
print(continuity)
"""   