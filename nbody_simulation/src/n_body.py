import sys
from pathlib import Path

# This line adds the real project root (the folder that contains both "main_folder" and "data")
PROJECT_ROOT = Path(__file__).resolve().parents[1]  # ← two levels up from main.py
sys.path.insert(0, str(PROJECT_ROOT))

from data.solar_system_data import *
from data.initial_conditions import *

class Body:
    G = 6.674e-11
    dt = 1e+5

    def __init__(self, name, trail_color, mass, x, y, z, v_x, v_y, v_z):

        self.name = name
        self.trail_color = trail_color
        self.mass = mass
        self.x = x
        self.y = y
        self.z = z
        self.v_x = v_x
        self.v_y = v_y
        self.v_z = v_z


def register_body(name):

    name = next((body[0] for body in bodies_data if body[0] == name), None)
    trail_color = next((body[1] for body in bodies_data if body[0] == name), None)
    mass = next((body[2] for body in bodies_data if body[0] == name), None)
    x = next((body[1] for body in bodies_conditions if body[0] == name), None)
    y = next((body[2] for body in bodies_conditions if body[0] == name), None)
    z = next((body[3] for body in bodies_conditions if body[0] == name), None)
    v_x = next((body[4] for body in bodies_conditions if body[0] == name), None)
    v_y = next((body[5] for body in bodies_conditions if body[0] == name), None)
    v_z = next((body[6] for body in bodies_conditions if body[0] == name), None)

    return Body(name, trail_color, mass, x, y, z, v_x, v_y, v_z)


#  Choice of objects that are properly registered in both files.
names_data = {body[0] for body in bodies_data}
names_condition = {body[0] for body in bodies_conditions}
names = names_data & names_condition

#  TODO: Replace with usage of selected example file according to config file.
requested_bodies_names = {'Sun', 'Earth'}

#  Only picking names of objects that are required in config file and are registered in the simulation.
registered_objects_names = names & requested_bodies_names

#  The main array of the simulation that defines list of names of processed bodies.
BODIES = []

#  Formation of BODIES list (doesnt get changed later).
for body_name in registered_objects_names:
    BODIES.append(register_body(body_name))
