class Config:
    """
    This is the main configuration files that allow to change parameters of the manipulation.
    """

    time_step_adapt = False  # Makes time step of the simulation constant in RK4 method if True, dynamic if False.
    time_step = 1e+4  # Value of time step if constant parameter is set.
    time_limit = 1e+10  # Simulation time limit, duration of the simulation.
    soft_param = 1e+3  # Softening parameter of the simulation, a parameter in equation: time_step = soft_param/a_max.
    # curants_number = 1e-1  # Value of Courant`s stability parameter if dynamic time step is set. Keep between 0 and 1.
    method = 'LP'  # The intergation method. Either set to 'RK4' for Runge_Kutta_4 or 'LP' for Leapfrog.
    frequency = 10  # How many iterations pass between each record of bodies` positions (useful to save storage space).
    dimensions = 2  # number of dimensions in the simulation, keep either 2 or 3. If set to 2 simulation will ignore z
    # parameters and simulate a plane.
    list_of_bodies = "inner_planets_example.py"
