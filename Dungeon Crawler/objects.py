class Player:
    def __init__(self, username : str, location : list):
        self.username = username
        self.location = location
        self.current_hp = 100
        self.max_hp = 100
        self.base_dmg = 10
        self.upgrades = []

class Action:
    def __init__(self, name : str, action):
        self.name = name
        self.action = action

    def execute(self):
        self.action()

player = None
current_map = None