import keyboard as kb
import random as r
import os
import termcolor as tc
import map
import objects as o
import ascii
import flavor
import actions as a

ui_health_change = 0

active_hotkeys = {}

def main():
    start_campaign()

def start_campaign():

    clear()
    o.player = o.Player(input("Name the vessel: "), [])

    begin_playthrough()

def begin_playthrough():
    global current_map

    input(f"The {o.player.username} sets out on another journey...\n")

    active_hotkeys["W"] = kb.add_hotkey("W", lambda: explore_turn([o.player.location[0], o.player.location[1] - 1]))
    active_hotkeys["A"] = kb.add_hotkey("A", lambda: explore_turn([o.player.location[0] - 1, o.player.location[1]]))
    active_hotkeys["S"] = kb.add_hotkey("S", lambda: explore_turn([o.player.location[0], o.player.location[1] + 1]))
    active_hotkeys["D"] = kb.add_hotkey("D", lambda: explore_turn([o.player.location[0] + 1, o.player.location[1]]))
    active_hotkeys["I"] = kb.add_hotkey("I", view_inventory)

    a.generate_map()
    explore_turn(o.player.location)

    kb.wait("esc")

def explore_turn(new_location):
    global ui_health_change

    clear()

    if new_location[0] < 0 or new_location[1] < 0:
        draw_ui()
        return
    try:
        o.current_map.discovered[new_location[1]][new_location[0]] = True
    except IndexError:
        draw_ui()
        return

    o.player.location = [new_location[0], new_location[1]]

    ui_health_change = 0

    # Remove extraneous hotkeys
    if "E" in active_hotkeys.keys():
        kb.remove_hotkey(active_hotkeys["E"])
        del active_hotkeys["E"]

    if o.current_map.data[o.player.location[1]][o.player.location[0]].terrain.type == map.terrain_types.asteroids:
        o.player.current_hp -= 4
        ui_health_change -= 4

    if o.player.current_hp <= 0:
        o.player.current_hp = 0
        for hotkey in list(active_hotkeys.keys()):
            kb.remove_hotkey(hotkey)

    draw_ui()

def draw_ui():
    global ui_health_change

    current_tile = o.current_map.data[o.player.location[1]][o.player.location[0]]

    if ui_health_change > 0:
        health_color = "light_blue"
        health_text = [tc.colored(f"[The ship's hull is repaired for {ui_health_change} points.]", health_color) + generate_tc_padding(21, [ui_health_change * -1])]
    elif ui_health_change < 0:
        health_color = "light_magenta"
        health_text = [tc.colored(f"[The ship sustains {ui_health_change * -1} points of damage.]", health_color) + generate_tc_padding(20, [ui_health_change * -1])]
    else:
        health_color = "green"
        health_text = None

    if health_text is not None:
        report_text = current_tile.terrain.flavor + health_text
    else:
        report_text = current_tile.terrain.flavor

    status_text = [
        "Hull Integrity:",
        f"{o.player.current_hp:04}/{o.player.max_hp:04} " + ascii.create_health_bar(health_color, 15, o.player.current_hp, o.player.max_hp)
    ]

    action_text = ["[I] View ship statistics"]
    if current_tile.action is not None:
        action_text.append("[E] " + current_tile.action.name)
        active_hotkeys["E"] = kb.add_hotkey("E", lambda: take_action(current_tile.action))

    o.current_map.draw(o.player.location)
    print("")
    report_box = ascii.InfoBox("white", 60, 3, "Crew Report", report_text)
    status_box = ascii.InfoBox("light_blue", 29, 3, f"{o.player.username}: Status", status_text)
    interact_box = ascii.InfoBox("light_blue", 30, 2, "Actions", action_text)

    ascii.draw_message_box([report_box])
    ascii.draw_message_box([status_box, interact_box])
    if o.player.current_hp <= 0:
        death_box = ascii.InfoBox("light_magenta", 60, 1, f"The Destruction of the {o.player.username}", r.choice(flavor.death_text) + ["[ESC] Exit..."])
        ascii.draw_message_box([death_box])

def take_action(action):
    # Execute an action, then reload the current map
    action.execute()
    explore_turn(o.player.location)

def view_inventory():
    kb.press("Enter")
    input()
    kb.release("Enter")
    clear()
    inventory_text = [
        "Hull Integrity:",
        f"{o.player.current_hp:04}/{o.player.max_hp:04} " + ascii.create_health_bar("green", 27, o.player.current_hp, o.player.max_hp) + generate_tc_padding(19, None),
        f"Weapon: Mass Drivers [DMG/t {o.player.base_dmg}]"
    ]
    inventory_box = ascii.InfoBox("white", 60, 3, f"The Status of the {o.player.username}", inventory_text)
    ascii.draw_message_box([inventory_box])
    input("[Enter] Exit ")
    clear()
    draw_ui()

def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Hack to prevent breaking infobox borders; adjust on case-by-case basis
def generate_tc_padding(chars : int, variables : list):
    subtract_chars = 0
    if variables is not None:
        for variable in variables:
            subtract_chars += len(str(variable))
    pad_string = []
    for i in range(chars - subtract_chars):
        pad_string.append(" ")
    return "".join(pad_string)

main()
