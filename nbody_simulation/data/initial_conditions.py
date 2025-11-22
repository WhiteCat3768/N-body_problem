class InitialConditions:

    def __init__(self, name, x, y, z, speed_x, speed_y, speed_z):

        self.name = name
        self.x = x
        self.y = y
        self.z = z
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.speed_z = speed_z


sun__     = InitialConditions('Sun', 0, 0, 0, 0, 0, 0)
mercury__ = InitialConditions('Mercury', 1e+6, 0, 0, 0, 0, 1e+4)
venus__   = InitialConditions('Venus', 1e+7, 0, 0, 0, 0, 5e+3)
earth__   = InitialConditions('Earth', 1e+8, 0, 0, 0, 0, 2e+3)
mars__    = InitialConditions('Mars', 1e+9, 0, 0, 0, 0, 1e+3)
jupiter__ = InitialConditions('Jupiter', 1e+10, 0, 0, 0, 0, 5e+2)
saturn__  = InitialConditions('Saturn', 1e+11, 0, 0, 0, 0, 2e+2)
uranus__  = InitialConditions('Uranus', 1e+12, 0, 0, 0, 0, 1e+2)
neptune__ = InitialConditions('Neptune', 1e+13, 0, 0, 0, 0, 1e+1)