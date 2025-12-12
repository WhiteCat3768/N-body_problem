# All existing bodies that simulation draws from. Must be registered in "initial_conditions.py" to be simulated.

bodies_data = [
    #  (Name[string], color[tuple], mass[float])
    ('Sun', (255, 255, 0), 1.9885e30),      # Yellow
    ('Mercury', (169, 169, 169), 3.3011e23), # Gray
    ('Venus', (255, 228, 181), 4.8675e24),   # Pale orange
    ('Earth', (0, 191, 255), 5.9724e24),     # Blue
    ('Mars', (255, 69, 0), 6.4171e23),       # Red-orange
    ('Ceres', (128, 128, 128), 9.39e20),  # Medium gray
    ('Vesta', (119, 136, 153), 2.59e20),  # Slate gray
    ('Jupiter', (210, 180, 140), 1.8982e27), # Tan
    ('Saturn', (238, 232, 170), 5.6834e26),  # Pale yellow
    ('Uranus', (173, 216, 230), 8.681e25),   # Light blue
    ('Neptune', (65, 105, 225), 1.0241e26),  # Royal blue
    ('Pluto', (165, 42, 42), 1.303e22),      # Brown
]
