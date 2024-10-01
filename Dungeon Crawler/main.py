import keyboard as kb
import random as r
import os
import map
import objects
from flavor import location_text

player = None
current_map = None

def main():
    start_campaign()

def start_campaign():
    global player

    clear()
    player = objects.Player(input("Name the vessel: "), [], [])

    begin_playthrough()

def begin_playthrough():
    global current_map

    input(f"The {player.username} sets out on another journey...\n")
    current_map = map.Map(r.randint(10, 20), r.randint(10, 20))
    player.location = current_map.start_location

    kb.add_hotkey("W", lambda: explore_turn([player.location[0], player.location[1] - 1]))
    kb.add_hotkey("A", lambda: explore_turn([player.location[0] - 1, player.location[1]]))
    kb.add_hotkey("S", lambda: explore_turn([player.location[0], player.location[1] + 1]))
    kb.add_hotkey("D", lambda: explore_turn([player.location[0] + 1, player.location[1]]))

    explore_turn(player.location)
    kb.wait("esc")

def explore_turn(new_location):
    global player

    clear()
    player.location = [new_location[0] % current_map.x_dim, new_location[1] % current_map.y_dim]
    current_map.render(player.location)
    current_map.discovered[player.location[1]][player.location[0]] = True
    print(r.choice(location_text[current_map.data[player.location[1]][player.location[0]].terrain.name]))

def clear():
    os.system("cls" if os.name == "nt" else "clear")

main()