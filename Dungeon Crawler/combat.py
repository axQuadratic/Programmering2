import os
import objects as o
import ascii
import keyboard as kb
from map import terrain_types
from copy import deepcopy
from time import sleep
import threading as th

combat_box = ascii.InfoBox("red", 60, 7, "Combat!", [])
current_enemy = None

load_ready = False

def main():
    begin_combat()

def measure_loading_time():
    global load_ready

    sleep(0.5)
    load_ready = True

def begin_combat(player : o.Player, enemy : o.Enemy):
    global current_enemy

    kb.press("Enter")
    input()
    kb.release("Enter")

    timer_thread = th.Thread(target=measure_loading_time)
    timer_thread.start()
    while True:
        if not load_ready:
            clear()
            print("Loading encounter...\n[Press ENTER to continue...]")
            input()
        else:
            break

    
    current_enemy = deepcopy(enemy)
    current_enemy.current_hp *= o.map_count
    current_enemy.max_hp *= o.map_count
    current_enemy.base_dmg *= o.map_count

    for hotkey in list(o.active_hotkeys.keys()):
        kb.remove_hotkey(hotkey)

    clear()
    combat_box.lines = [f"The {player.username} is under attack by a {enemy.name}!"]
    draw_combat_box()
    input()

    while True:
        combat_turn()
        if o.player.current_hp <= 0 or current_enemy.current_hp <= 0:
            return

        input()

def combat_turn():
    clear()

    player_dmg = o.player.base_dmg - current_enemy.defense
    enemy_dmg = current_enemy.base_dmg - o.player.defense
    if player_dmg > 0: current_enemy.current_hp -= player_dmg
    if enemy_dmg > 0: o.player.current_hp -= enemy_dmg

    if current_enemy.current_hp <= 0:
        current_enemy.current_hp = 0
        o.current_map.data[o.player.location[1]][o.player.location[0]].terrain.set_type(terrain_types.defeated)
        combat_box.lines = [f"The {current_enemy.name} was destroyed!"]
    elif o.player.current_hp <= 0:
        o.player.current_hp = 0
        combat_box.lines = [f"The {o.player.username} receives critical hull damage..."]
    else:
        combat_box.lines = [""]

    draw_combat_box()

def draw_combat_box():
    combat_box.lines.append(f"{o.player.username}: {o.player.current_hp}/{o.player.max_hp}")
    combat_box.lines.append(ascii.create_health_bar("light_blue", 56, o.player.current_hp, o.player.max_hp))
    combat_box.lines.append(f"{current_enemy.name}: {current_enemy.current_hp}/{current_enemy.max_hp}")
    combat_box.lines.append(ascii.create_health_bar("light_red", 56, current_enemy.current_hp, current_enemy.max_hp))

    combat_box.lines.append("[Enter] Continue")
    ascii.draw_message_box([combat_box])

def clear():
    os.system("cls" if os.name == "nt" else "clear")