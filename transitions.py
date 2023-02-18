from math import sin, cos, pi, sqrt

class Transitions:
    def ease_in_out_sine(self, current_time, start_value, change_in_value, duration):
        calc = 1-change_in_value/2 * (cos(pi*current_time/duration) - 1) + start_value
        return int(calc)

    def ease_in_cubic(self, current_time, start_value, change_in_value, duration):
        current_time /= duration
        calc = change_in_value*current_time*current_time*current_time + start_value
        return int(calc)