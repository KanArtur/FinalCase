from math import sin, pi


class Value:
    def __int__(self):
        self.oxi = 7
        self.fuel = 10


class Speed:
    def __init__(self):
        global weight, power, max_power, gn
        self.speed = 2 * (200 / (192 + gn)) * (((power / max_power) * 100) / 80)


class Ratio:
    def __init__(self):
        global temp, oxi
        self.ratio = sin((-pi / 2) + (pi * (temp + (0.5 * oxi))) / 40)


class Population:
    def __init__(self):
        global old_population, ratio
        self.population = old_population + old_population  * ratio


class Electricity:
    def __init__(self):
        self.electricity = 0
        for i in range(temp + 1):
            self.electricity += i