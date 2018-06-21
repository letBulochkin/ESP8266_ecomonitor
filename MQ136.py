from MQ_Base import MQ

class MQ136(MQ):
    """
    MicroPython library to deal with MQ-136 H2S sensor.
    For complete algorithm refer to MQ_Base.py
    Parameters for ppm and temperature correction calculations are taken
    by approximation of the curves given in sensor datasheet: vk.cc/8c3WqU

    TODO: check RLOAD, RZERO
    """

    def __init__(self, pin):
        self.pin = pin
        self.RLOAD = 10.0
        self.RZERO = 0.0000005638
        self.PPMPARA = 0.5907
        self.PPMPARB = -0.2675
        self.THPARA = -0.014
        self.THPARB = -0.0076
        self.THPARC = 1.812
