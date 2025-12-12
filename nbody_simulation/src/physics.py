from config.config import Config

G = 6.674e-11


def acceleration_diff(self, bodies):
    acceleration_x = 0
    acceleration_y = 0
    acceleration_z = 0

    for body_2 in bodies:
        if self.name != body_2.name:
            acceleration = (G * body_2.mass) / (
                        ((self.x - body_2.x) ** 2 + (self.y - body_2.y) ** 2 + (self.z - body_2.z) ** 2) ** 1.5)
            acceleration_x -= acceleration * (self.x - body_2.x)
            acceleration_y -= acceleration * (self.y - body_2.y)
            acceleration_z -= acceleration * (self.z - body_2.z)

    return acceleration_x, acceleration_y, acceleration_z


def speed_update(acceleration_x, acceleration_y, acceleration_z, dt):
    delta_speed_x = acceleration_x * dt
    delta_speed_y = acceleration_y * dt
    delta_speed_z = acceleration_z * dt

    return delta_speed_x, delta_speed_y, delta_speed_z


def position_update(speed_x, speed_y, speed_z, dt):
    delta_x = speed_x * dt
    delta_y = speed_y * dt
    delta_z = speed_z * dt

    return delta_x, delta_y, delta_z


def calculate_time_step(bodies):
    a_max = 0
    for body in bodies:
        a_x, a_y, a_z = acceleration_diff(body, bodies)
        a_max = max(a_max, (a_x ** 2 + a_y ** 2 + a_z ** 2) ** 0.5)

    time_step = Config.soft_param / a_max

    return time_step
