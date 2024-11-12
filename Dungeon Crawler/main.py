import keyboard as kb
import random as r
import os
import termcolor as tc
import map
import objects as o
import ascii
import flavor
import actions as a
import combat as c

ui_health_change = 0

def main():
    start_campaign()

def start_campaign():

    clear()
    o.player = o.Player(input("Name the vessel: "), [])

    begin_playthrough()

def begin_playthrough():
    global current_map

    input(f"The {o.player.username} sets out on another journey...\n")

    create_movement_hotkeys()

    a.generate_map()
    explore_turn(o.player.location)

    kb.wait("esc")

def create_movement_hotkeys():
    o.active_hotkeys["8"] = kb.add_hotkey("8", lambda: explore_turn([o.player.location[0], o.player.location[1] - 1]))
    o.active_hotkeys["4"] = kb.add_hotkey("4", lambda: explore_turn([o.player.location[0] - 1, o.player.location[1]]))
    o.active_hotkeys["2"] = kb.add_hotkey("2", lambda: explore_turn([o.player.location[0], o.player.location[1] + 1]))
    o.active_hotkeys["6"] = kb.add_hotkey("6", lambda: explore_turn([o.player.location[0] + 1, o.player.location[1]]))
    o.active_hotkeys["7"] = kb.add_hotkey("7", lambda: explore_turn([o.player.location[0] - 1, o.player.location[1] - 1]))
    o.active_hotkeys["9"] = kb.add_hotkey("9", lambda: explore_turn([o.player.location[0] + 1, o.player.location[1] - 1]))
    o.active_hotkeys["1"] = kb.add_hotkey("1", lambda: explore_turn([o.player.location[0] - 1, o.player.location[1] + 1]))
    o.active_hotkeys["3"] = kb.add_hotkey("3", lambda: explore_turn([o.player.location[0] + 1, o.player.location[1] + 1]))
    o.active_hotkeys["I"] = kb.add_hotkey("I", view_inventory)

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
    if "E" in o.active_hotkeys.keys():
        kb.remove_hotkey(o.active_hotkeys["E"])
        del o.active_hotkeys["E"]

    terrain_type = o.current_map.data[o.player.location[1]][o.player.location[0]].terrain.type
    if terrain_type == map.terrain_types.asteroids:
        o.player.current_hp -= 4
        ui_health_change -= 4

    if terrain_type == map.terrain_types.hostile:
        c.begin_combat(o.player, r.choice(o.enemies))
        input()
        clear()
        create_movement_hotkeys()

    if o.player.current_hp <= 0:
        o.player.current_hp = 0
        for hotkey in list(o.active_hotkeys.keys()):
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
        o.active_hotkeys["E"] = kb.add_hotkey("E", lambda: take_action(current_tile.action))

    o.current_map.draw(o.player.location)
    print("")
    report_box = ascii.InfoBox("white", 60, 3, "Crew Report", report_text)
    status_box = ascii.InfoBox("light_blue", 29, 3, f"{o.player.username}: Status", status_text)
    interact_box = ascii.InfoBox("light_blue", 30, 2, "Actions", action_text)

    ascii.draw_message_box([report_box])
    ascii.draw_message_box([status_box, interact_box])
    if o.player.current_hp <= 0:
        death_box = ascii.InfoBox("light_magenta", 60, 1, f"The Destruction of the {o.player.username}", r.choice(flavor.death_text) + [f"[You survived {o.map_count} sectors.]","[ESC] Exit..."])
        ascii.draw_message_box([death_box])
    if o.upgrade_box is not None:
        ascii.draw_message_box([o.upgrade_box])
        o.upgrade_box = None

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
        f"Weapon: Mass Drivers [DMG/t {o.player.base_dmg}]",
        f"Overshield Strength: {o.player.defense}",
        f"Sectors Survived: {o.map_count}"
    ]
    inventory_box = ascii.InfoBox("white", 60, 5, f"The Status of the {o.player.username}", inventory_text)
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
