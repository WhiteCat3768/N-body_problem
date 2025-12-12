# All existing bodies that simulation draws from. Must be registered in "solar_system_data.py" to be simulated.

bodies_conditions = [
    #  (Name[string], x_coordinate[float], y_coordinate[float], z_coordinate[float], x_speed[float], y_speed[float],
    #  z_speed[float])
    ('Sun',         0.0            , 0.0, 0.0, 0.0,  0.0  , 0.0),
    ('Mercury',     5.7909227e+10  , 0.0, 0.0, 0.0, -47360, 0.0),
    ('Venus',       1.0820893e+11  , 0.0, 0.0, 0.0, -35020, 0.0),
    ('Earth',       1.495978707e+11, 0.0, 0.0, 0.0, -29780, 0.0),
    ('Mars',        2.279392e+11   , 0.0, 0.0, 0.0, -24070, 0.0),
    ('Ceres',       4.1388e+11     , 0.0, 0.0, 0.0, -17890, 0.0),
    ('Vesta',       3.5325e+11     , 0.0, 0.0, 0.0, -19210, 0.0),
    ('Jupiter',     7.785e+11      , 0.0, 0.0, 0.0, -13070, 0.0),
    ('Saturn',      1.4267e+12     , 0.0, 0.0, 0.0,  -9640, 0.0),
    ('Uranus',      2.8707e+12     , 0.0, 0.0, 0.0,  -6810, 0.0),
    ('Neptune',     4.4984e+12     , 0.0, 0.0, 0.0,  -5430, 0.0),
    ('Pluto',       5.9064e+12     , 0.0, 0.0, 0.0,  -4730, 0.0)
]
