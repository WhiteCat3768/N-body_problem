from physics import *

"""
This is a standard Leapfrog algorithm.
Calculations are split into the first half-step to calculate initial speed and the second full step cycle.
Done to keep number of data structures in the project as low as possible and server the main Body class.
"""


def pre_leapfrog(bodies, dt):

    #  Initial half-step for calculation initial velocity.
    for i in range(len(bodies)):

        a_x, a_y, a_z = acceleration_diff(bodies[i], bodies)

        delta_v_x, delta_v_y, delta_v_z = speed_update(a_x, a_y, a_z, dt/2)
        bodies[i].v_x += delta_v_x
        bodies[i].v_y += delta_v_y
        bodies[i].v_z += delta_v_z

    return bodies


def leapfrog(bodies, dt):

    #  Main step for calculating new values of positions and values of simulated bodies.
    for i in range(len(bodies)):

        delta_x, delta_y, delta_z = position_update(bodies[i].v_x, bodies[i].v_y, bodies[i].v_z, dt)
        bodies[i].x += delta_x
        bodies[i].y += delta_y
        bodies[i].z += delta_z

    for i in range(len(bodies)):

        a_x, a_y, a_z = acceleration_diff(bodies[i], bodies)

        delta_v_x, delta_v_y, delta_v_z = speed_update(a_x, a_y, a_z, dt/2)
        bodies[i].v_x += delta_v_x
        bodies[i].v_y += delta_v_y
        bodies[i].v_z += delta_v_z

    return bodies
