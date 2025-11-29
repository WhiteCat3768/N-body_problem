G = 6.674e-11

def Acceleration_diff(self, bodies):

    acceleration_x = 0
    acceleration_y = 0
    acceleration_z = 0

    for body_2 in bodies:
        if self.name != body_2.name:
            acceleration = (G * body_2.mass) / (((self.x - body_2.x) ** 2 + (self.y - body_2.y) ** 2 + self.z - body_2.z) ** 2) ** 1.5)
            acceleration_x += acceleration * (body_2.x - self.x)
            acceleration_y += acceleration * (body_2.y - self.y)
            acceleration_z += acceleration * (body_2.z - self.z)

    return(acceleration_x, acceleration_y, acceleration_z)

def Speed_diff(self, acceleration_x, acceleration_y, acceleration_z, dt):

    delta_speed_x = acceleration_x * dt
    delta_speed_y = acceleration_y * dt
    delta_speed_z = acceleration_z * dt

    return(delta_speed_x, delta_speed_y, delta_speed_z)

def Position_diff(self, speed_x, speed_y, speed_z, dt):

    delta_x = speed_x * dt
    delta_y = speed_y * dt
    delta_z = speed_z * dt

    return(delta_x, delta_y, delta_z)
