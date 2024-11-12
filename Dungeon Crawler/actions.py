import random as r
import objects as o
import ascii

def generate_map():
    from map import Map # This import is buffered to prevent circular import errors

    o.map_count += 1
    o.current_map = Map(r.randint(7, 15), r.randint(7, 15))
    o.player.location = o.current_map.start_location

def receive_upgrade():
    from map import terrain_types
    
    o.upgrade_box = ascii.InfoBox("light_green", 60, 2, f"{o.player.username}: Upgraded!", [])
    upgrade = r.randint(1, 3)
    if upgrade == 1:
        dmg = r.randint(5, 10)
        o.player.base_dmg += dmg
        o.upgrade_box.lines.append(f"The ship's weapon damage has been upgraded by {dmg} points.")

    elif upgrade == 2:
        hp = r.randint(5, 15)
        o.player.max_hp += hp
        o.player.current_hp += hp
        o.upgrade_box.lines.append(f"The ship's hull integrity has been improved by {hp} points.")

    elif upgrade == 3:
        defense = r.randint(1, 3)
        o.player.defense += defense
        o.upgrade_box.lines.append(f"The ship's overshield is now {defense} points stronger.")

    o.upgrade_box.lines.append("Repairs have also been made.")

    repair()

    o.current_map.data[o.player.location[1]][o.player.location[0]].terrain.set_type(terrain_types.trade_post_empty)
    o.current_map.data[o.player.location[1]][o.player.location[0]].action = None

def repair():
    o.player.current_hp += round(o.player.max_hp / 2)
    if o.player.current_hp > o.player.max_hp:
        o.player.current_hp = o.player.max_hp

a_next_map = o.Action("Proceed to next sector", generate_map)
a_receive_upgrade = o.Action("Repair & apply upgrade", receive_upgrade)
a_repair = o.Action("Repair ship", repair)