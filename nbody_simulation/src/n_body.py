import sys
from pathlib import Path

# This line adds the real project root (the folder that contains both "main_folder" and "data")
PROJECT_ROOT = Path(__file__).resolve().parents[1]   # ← two levels up from main.py
sys.path.insert(0, str(PROJECT_ROOT))

from data.solar_system_data import *
from data.initial_conditions import *

#  from physics import *

class Body:
    G = 6.674e-11
    bodies = []
    dt = 1e+5

    def __init__(self, name, trail_color, mass, x, y, z, speed_x, speed_y, speed_z):

        Body.bodies.append(self)

        self.name = name
        self.trail_color = trail_color
        self.mass = mass
        self.x = x
        self.y = y
        self.z = z
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.speed_z = speed_z
        self.trail = []

def Register_body(name, trail_color, mass, x, y, z, speed_x, speed_y, speed_z, trail):

    pass
    #  return body

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
    BODIES.append(Register_body(next((body[0] for body in bodies_data if body[0] == body_name), None),
                                next((body[1] for body in bodies_data if body[0] == body_name), None),
                                next((body[2] for body in bodies_data if body[0] == body_name), None),
                                next((body[1] for body in bodies_conditions if body[0] == body_name), None),
                                next((body[2] for body in bodies_conditions if body[0] == body_name), None),
                                next((body[3] for body in bodies_conditions if body[0] == body_name), None),
                                next((body[4] for body in bodies_conditions if body[0] == body_name), None),
                                next((body[5] for body in bodies_conditions if body[0] == body_name), None),
                                next((body[6] for body in bodies_conditions if body[0] == body_name), None),
                                []
                                ))
