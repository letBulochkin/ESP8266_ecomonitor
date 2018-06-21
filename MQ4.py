from MQ_Base import MQ

class MQ4(MQ):
    """
    MicroPython library to deal with MQ-4 CH4 sensor.
    For complete algorithm refer to MQ_Base.py
    Parameters for ppm and temperature correction calculations are taken
    by approximation of the curves given in sensor datasheet: vk.cc/8c4bHG

    TODO: check RLOAD, RZERO
    """

    def __init__(self, pin):
        self.pin = pin
        self.RLOAD = 10.0  # to be corrected 
        self.RZERO = 0.0000005638  # to be measured
        self.PPMPARA = 6.9743
        self.PPMPARB = -0.6049
        self.THPARA = -0.0139
        self.THPARB = -0.0076
        self.THPARC = 1.8099
