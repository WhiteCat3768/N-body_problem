import matplotlib.pyplot as plt


class Body:
    G = 6.674e-11
    bodies = []
    dt = 1e+5

    def __init__(self, name, trail_color, mass, x, y, speed_x, speed_y):

        Body.bodies.append(self)

        self.name = name
        self.trail_color = trail_color
        self.mass = mass
        self.x = x
        self.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.trail = []

    def define(self):
        print(f"Object {self.name} is located at x: {self.x} and y: {self.y}, is moving with "
              f"{(self.speed_x ** 2 + self.speed_y ** 2) ** 0.5} speed.")

    def explicit_euler(self):
        acceleration_x = 0
        acceleration_y = 0

        for body_2 in Body.bodies:
            if self.name != body_2.name:
                acceleration = (Body.G * body_2.mass) / (((self.x - body_2.x) ** 2 + (self.y - body_2.y) ** 2) ** 1.5)
                acceleration_x += acceleration * (body_2.x - self.x)
                acceleration_y += acceleration * (body_2.y - self.y)

        self.move(acceleration_x, acceleration_y)

    def move(self, acceleration_x, acceleration_y):
        self.speed_x += acceleration_x * Body.dt
        self.speed_y += acceleration_y * Body.dt
        self.x += self.speed_x * Body.dt
        self.y += self.speed_y * Body.dt
        self.trail.append((self.x, self.y))


iteration = 1
time_limit = 1e+9

sun = Body('Sun', 'yellow', 1.98e30, 0, 0, 0, 0)
mercury = Body('Mercury', 'red', 3.30e23, 5.79e10, 0, 0, 47400)
venus = Body('Venus', 'orange', 4.87e24, 1.08e11, 0, 0, 35000)

for t in range(int(time_limit / Body.dt)):
    for body in Body.bodies:
        body.explicit_euler()
    iteration += 1

    if iteration // 1000 == 0:
        for i in Body.bodies:
            i.define()

plt.figure(figsize=(10, 10))
for body in Body.bodies:
    if body.trail:
        xs, ys = zip(*body.trail)
        plt.plot(xs, ys, color=body.trail_color, label=body.name, linewidth=0.8)
        plt.scatter([xs[0]], [ys[0]], color=body.trail_color, s=50, zorder=5)
        plt.scatter([xs[-1]], [ys[-1]], color=body.trail_color, s=50, zorder=5)

plt.xlabel('X (m)')
plt.ylabel('Y (m)')
plt.title('Orbital Trajectories')
plt.legend()
plt.grid(True, alpha=0.3)
plt.axis('equal')
plt.show()
