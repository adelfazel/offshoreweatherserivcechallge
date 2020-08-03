import logging
import math

logger = logging.getLogger('globalLogger')


def rad_to_degree(rad): return rad * 180 / math.pi


class WindRecord:
    def __init__(self, time, horizontal_speed, vertical_speed):
        self.time = time
        self.horizontal_speed = float(horizontal_speed)
        self.vertical_speed = float(vertical_speed)

    def get_time(self):
        return self.time

    def get_phi_rads(self):
        return math.atan2(-self.horizontal_speed, -self.vertical_speed)

    def get_wind_speed(self):
        return math.sqrt(self.horizontal_speed ** 2 + self.vertical_speed ** 2)

    def get_wind_direction_deg(self):
        return rad_to_degree(self.get_phi_rads())

    def __str__(self):
        return f"time:{self.time} horizontal: {self.horizontal_speed} vertical:{self.vertical_speed}"



