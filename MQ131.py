from MQ_Base import MQ

class MQ131(MQ):
    """
    MicroPython library to deal with MQ-131 ozone sensor.
    For complete algorithm refer to MQ_Base.py
    Parameters for ppm and temperature correction calculations are taken
    by approximation of the curves given in sensor datasheet: vk.cc/8c4flT

    TODO: check RLOAD, RZERO
    """

    def __init__(self, pin):
        self.pin = pin
        self.RLOAD = 4.7  # to be corrected 
        self.RZERO = 1259.11
        self.PPMPARA = 0.4015
        self.PPMPARB = 0.4289
        self.THPARA = -0.0139
        self.THPARB = -0.0076
        self.THPARC = 1.8104
