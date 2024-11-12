class Character:
    def __init__(self, current_hp, max_hp, base_dmg, defense):
        self.current_hp = current_hp
        self.max_hp = max_hp
        self.base_dmg = base_dmg
        self.defense = defense

class Player(Character):
    def __init__(self, username : str, location : list):
        super().__init__(100, 100, 10, 0)
        self.username = username
        self.location = location
        self.upgrades = []

class Enemy(Character):
    def __init__(self, name, icon, max_hp, damage, defense):
        super().__init__(max_hp, max_hp, damage, defense)
        self.name = name
        self.icon = icon

class Action:
    def __init__(self, name : str, action):
        self.name = name
        self.action = action

    def execute(self):
        self.action()

player = None
current_map = None
map_count = 0

active_hotkeys = {}

upgrade_box = None

enemies = [
    Enemy("Raiding Party", "r", 10, 1, 0),
    Enemy("Raiding Fleet", "R", 25, 2, 0),
    Enemy("Raiding Freighter", "F", 50, 5, 0),
]