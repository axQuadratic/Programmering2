import objects as o
import random as r

def generate_map():
    from map import Map # This import is buffered to prevent circular import errors

    o.current_map = Map(r.randint(7, 15), r.randint(7, 15))
    o.player.location = o.current_map.start_location

a_next_map = o.Action("Proceed to next sector", generate_map)