class Character:
    def __init__(self, current_hp, max_hp, base_dmg):
        self.current_hp = current_hp
        self.max_hp = max_hp
        self.base_dmg = base_dmg

class Player(Character):
    def __init__(self, username : str, location : list):
        super().__init__(100, 100, 10)
        self.username = username
        self.location = location
        self.upgrades = []

class Enemy(Character):
    def __init__(self, name, icon, max_hp, damage):
        super().__init__(max_hp, max_hp, damage)
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

enemies = [
    Enemy("Raiding Party"),
    Enemy("Raiding Fleet"),
    Enemy("Raider Freighter")
]