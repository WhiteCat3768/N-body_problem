import sys
from pathlib import Path

# This line adds the real project root (the folder that contains both "main_folder" and "data")
PROJECT_ROOT = Path(__file__).resolve().parents[1]   # ← two levels up from main.py
sys.path.insert(0, str(PROJECT_ROOT))

from data.solar_system_data import *
from data.initial_conditions import *

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


# The following part is entirely a placeholder and will be rewritten to support custom names and any amount of objects.

sun = Body(sun_.name, sun_.trail_color, sun_.mass, sun__.x, sun__.y, sun__.z, sun__.speed_x, sun__.speed_y, sun__.speed_z)
mercury = Body(mercury_.name, mercury_.trail_color, mercury_.mass, mercury__.x, mercury__.y, mercury__.z, mercury__.speed_x, mercury__.speed_y, mercury__.speed_z)
venus = Body(venus_.name, venus_.trail_color, venus_.mass, venus__.x, venus__.y, venus__.z, venus__.speed_x, venus__.speed_y, venus__.speed_z)
earth = Body(earth_.name, earth_.trail_color, earth_.mass, earth__.x, earth__.y, earth__.z, earth__.speed_x, earth__.speed_y, earth__.speed_z)
mars = Body(mars_.name, mars_.trail_color, mars_.mass, mars__.x, mars__.y, mars__.z, mars__.speed_x, mars__.speed_y, mars__.speed_z)
jupiter = Body(jupiter_.name, jupiter_.trail_color, jupiter_.mass, jupiter__.x, jupiter__.y, jupiter__.z, jupiter__.speed_x, jupiter__.speed_y, jupiter__.speed_z)
saturn = Body(saturn_.name, saturn_.trail_color, saturn_.mass, saturn__.x, saturn__.y, saturn__.z, saturn__.speed_x, saturn__.speed_y, saturn__.speed_z)
uranus = Body(uranus_.name, uranus_.trail_color, uranus_.mass, uranus__.x, uranus__.y, uranus__.z, uranus__.speed_x, uranus__.speed_y, uranus__.speed_z)
neptune = Body(neptune_.name, neptune_.trail_color, neptune_.mass, neptune__.x, neptune__.y, neptune__.z, neptune__.speed_x, neptune__.speed_y, neptune__.speed_z)
