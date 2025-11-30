from n_body import Body
from physics import *


def rk_4(bodies, dt):

    #  Initialization of virtual bodies for stages of the method.
    bodies_0 = bodies[:]
    bodies_1 = bodies[:]
    bodies_2 = bodies[:]
    bodies_3 = bodies[:]
    bodies_4 = bodies[:]

    #  First stage of the method.
    for i in range(len(bodies)):

        a_x, a_y, a_z = acceleration_diff(bodies_0[i], bodies_0)

        delta_v_x, delta_v_y, delta_v_z = speed_update(a_x, a_y, a_z, dt/2)
        bodies_1[i].v_x += delta_v_x
        bodies_1[i].v_y += delta_v_y
        bodies_1[i].v_z += delta_v_z

        delta_x, delta_y, delta_z = position_update(bodies_1[i].v_x, bodies_1[i].v_y, bodies_1[i].v_z, dt/2)
        bodies_1[i].x += delta_x
        bodies_1[i].y += delta_y
        bodies_1[i].z += delta_z

    # Second stage of the method.
    for i in range(len(bodies)):

        a_x, a_y, a_z = acceleration_diff(bodies_1[i], bodies_1)

        delta_v_x, delta_v_y, delta_v_z = speed_update(a_x, a_y, a_z, dt/2)
        bodies_2[i].v_x += delta_v_x
        bodies_2[i].v_y += delta_v_y
        bodies_2[i].v_z += delta_v_z

        delta_x, delta_y, delta_z = position_update(bodies_2[i].v_x, bodies_2[i].v_y, bodies_2[i].v_z, dt/2)
        bodies_2[i].x += delta_x
        bodies_2[i].y += delta_y
        bodies_2[i].z += delta_z

    # Third stage of the method.
    for i in range(len(bodies)):

        a_x, a_y, a_z = acceleration_diff(bodies_2[i], bodies_2)

        delta_v_x, delta_v_y, delta_v_z = speed_update(a_x, a_y, a_z, dt)
        bodies_3[i].v_x += delta_v_x
        bodies_3[i].v_y += delta_v_y
        bodies_3[i].v_z += delta_v_z

        delta_x, delta_y, delta_z = position_update(bodies_2[i].v_x, bodies_2[i].v_y, bodies_2[i].v_z, dt)
        bodies_3[i].x += delta_x
        bodies_3[i].y += delta_y
        bodies_3[i].z += delta_z

    # Forth stage of the method.
    for i in range(len(bodies)):

        a_x, a_y, a_z = acceleration_diff(bodies_3[i], bodies_3)

        delta_v_x, delta_v_y, delta_v_z = speed_update(a_x, a_y, a_z, dt)
        bodies_4[i].v_x += delta_v_x
        bodies_4[i].v_y += delta_v_y
        bodies_4[i].v_z += delta_v_z

        delta_x, delta_y, delta_z = position_update(bodies_3[i].v_x, bodies_3[i].v_y, bodies_3[i].v_z, dt)
        bodies_4[i].x += delta_x
        bodies_4[i].y += delta_y
        bodies_4[i].z += delta_z

    #  Calculation of real change of speed and position.
    #  Changes are not saved separately, but rather acquired through difference between virtual and real values.
    for i in range(len(bodies)):

        bodies[i].v_x = (1 / 6) * (bodies_1[i].v_x + 2 * bodies_2[i].v_x + 2 * bodies_3[i].v_x + bodies_4[i].v_x -
                                   - 6 * bodies_0[i].v_x)
        bodies[i].v_y = (1 / 6) * (bodies_1[i].v_y + 2 * bodies_2[i].v_y + 2 * bodies_3[i].v_y + bodies_4[i].v_y -
                                   - 6 * bodies_0[i].v_y)
        bodies[i].v_z = (1 / 6) * (bodies_1[i].v_z + 2 * bodies_2[i].v_z + 2 * bodies_3[i].v_z + bodies_4[i].v_z -
                                   - 6 * bodies_0[i].v_z)

        bodies[i].x = (1 / 6) * (bodies_1[i].x + 2 * bodies_2[i].x + 2 * bodies_3[i].x + bodies_4[i].x -
                                   - 6 * bodies_0[i].x)
        bodies[i].y = (1 / 6) * (bodies_1[i].y + 2 * bodies_2[i].y + 2 * bodies_3[i].y + bodies_4[i].y -
                                   - 6 * bodies_0[i].y)
        bodies[i].z = (1 / 6) * (bodies_1[i].z + 2 * bodies_2[i].z + 2 * bodies_3[i].z + bodies_4[i].z -
                                   - 6 * bodies_0[i].z)

    return bodies
