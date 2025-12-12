import importlib
import sys
from collections import defaultdict
from pathlib import Path
import matplotlib.pyplot as plt

# This line adds the real project root (the folder that contains both "main_folder" and "data")
PROJECT_ROOT = Path(__file__).resolve().parents[1]  # ← two levels up from main.py
sys.path.insert(0, str(PROJECT_ROOT))

from data.solar_system_data import bodies_data
from data.initial_conditions import bodies_conditions

from rk4_integrator import *
from leapfrog_integrator import *

from config.config import Config

# Gets list of bodies to be simulated from a specified example file.
body_list_name = Config.list_of_bodies
if body_list_name[-3:] == '.py':
    body_list_name = body_list_name[:-3]
bodies_file = importlib.import_module(f"examples.{body_list_name}")
list_of_bodies = bodies_file.list_of_bodies


class Body:
    G = 6.674e-11

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


def register_body_2d(name):
    name = next((body[0] for body in bodies_data if body[0] == name), None)
    trail_color = next((tuple(c / 255.0 for c in body[1]) for body in bodies_data if body[0] == name), None)
    mass = next((body[2] for body in bodies_data if body[0] == name), None)
    x = next((body[1] for body in bodies_conditions if body[0] == name), None)
    y = next((body[2] for body in bodies_conditions if body[0] == name), None)
    v_x = next((body[4] for body in bodies_conditions if body[0] == name), None)
    v_y = next((body[5] for body in bodies_conditions if body[0] == name), None)

    return Body(name, trail_color, mass, x, y, 0, v_x, v_y, 0)


def register_body_3d(name):
    name = next((body[0] for body in bodies_data if body[0] == name), None)
    trail_color = next((tuple(c / 255.0 for c in body[1]) for body in bodies_data if body[0] == name), None)
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
registered_names = names_data & names_condition

# Only picking names of objects that are required in config file and are registered in the simulation.
registered_objects_names = registered_names & list_of_bodies

# The main array of the simulation that defines list of names of processed bodies.
BODIES = []

# Dictionaries that contains trails of coordinates of bodies to be displayed later on the graph.
x_trails = defaultdict(list)
y_trails = defaultdict(list)
z_trails = defaultdict(list)

# Formation of BODIES list (doesnt get changed later) and list of trajectory trails.
for body_name in registered_objects_names:
    if Config.dimensions == 3:
        BODIES.append(register_body_3d(body_name))
    else:
        BODIES.append(register_body_2d(body_name))

"""
Beginning of the main simulation loop. By now the main BODIES class is formed.
"""

t = 0
iteration = 0

if Config.method == 'RK4':

    while t < Config.time_limit:

        if Config.time_step_adapt:
            time_step = calculate_time_step(BODIES)
            t += time_step
            BODIES = rk_4(BODIES, time_step)
        else:
            time_step = Config.time_step
            t += time_step
            BODIES = rk_4(BODIES, time_step)
        iteration += 1

        if iteration % Config.frequency == 0:
            for body in BODIES:
                x_trails[body.name].append(body.x)
                y_trails[body.name].append(body.y)
                z_trails[body.name].append(body.z)

            print(
                f"Iteration {iteration}, simulated {t:.0f}s of {Config.time_limit:.0f}s, "
                f"{(t / Config.time_limit) * 100:.6f}% done.")

if Config.method == 'LP':

    BODIES = pre_leapfrog(BODIES, Config.time_step)

    while t < Config.time_limit:

        BODIES = leapfrog(BODIES, Config.time_step)
        t += Config.time_step
        iteration += 1

        if iteration % Config.frequency == 0:
            for body in BODIES:
                x_trails[body.name].append(body.x)
                y_trails[body.name].append(body.y)
                z_trails[body.name].append(body.z)

            print(
                f"Iteration {iteration}, simulated: {t:.0f}s of {Config.time_limit:.0f}s, "
                f"{(t / Config.time_limit) * 100:.6f}% done.")

print(f"Simulation finished, output file saved in {1}. Vizualizing trails.")

"""
Visualizes the trails of bodies in 2D or 3D, depending on the config.
"""
fig = plt.figure(figsize=(10, 8))

if Config.dimensions == 3:
    ax = fig.add_subplot(111, projection='3d')

    for body in BODIES:
        x_data = x_trails[body.name]
        y_data = y_trails[body.name]
        z_data = z_trails[body.name]
        ax.plot(x_data, y_data, z_data, label=body.name, color=body.trail_color)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

elif Config.dimensions == 2:
    ax = fig.add_subplot(111)

    for body in BODIES:
        x_data = x_trails[body.name]
        y_data = y_trails[body.name]
        ax.plot(x_data, y_data, label=body.name, color=body.trail_color)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')

    ax.set_aspect('equal', adjustable='box')
    

ax.legend()
plt.title(f'Trail Visualization')
plt.show()
