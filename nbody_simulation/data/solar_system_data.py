class Data:

    def __init__(self, name, trail_color, mass):

        self.name = name
        self.trail_color = trail_color
        self.mass = mass


sun     = Data('Sun',     'gold',        1.9885e+30)
mercury = Data('Mercury', 'gray',        3.3011e+23)
venus   = Data('Venus',   'yellow',      4.8675e+24)
earth   = Data('Earth',   'blue',        5.9724e+24)
mars    = Data('Mars',    'red',         6.4171e+23)
jupiter = Data('Jupiter', 'orange',      1.8982e+27)
saturn  = Data('Saturn',  'yellow',      5.6834e+26)
uranus  = Data('Uranus',  'cyan',        8.6810e+25)
neptune = Data('Neptune', 'blue',        1.0241e+26)
