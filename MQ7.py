from MQ_Base import MQ

class MQ7(MQ):
    """
    MicroPython library to deal with MQ-7 Troyka CO sensor.
    For complete algorithm refer to MQ_Base.py
    Parameters for ppm and temperature correction calculations are taken
    by approximation of the curves given in sensor datasheet:
    wiki.amperka.ru/_media/%D0%BF%D1%80%D0%BE%D0%B4%D1%83%D0%BA%D1%82%D1%8B:mq7:troyka-mq7_datasheet.pdf
    RLoad value taken from Troyka MQ libraries implementation: github.com/amperka/TroykaMQ
    """

    def __init__(self, pin):
        self.pin = pin
        self.RLOAD = 10.0
        self.RZERO = 7.55
        self.PPMPARA = 29.4544
        self.PPMPARB = -0.778
        self.THPARA = -0.0068
        self.THPARB = -0.0035
        self.THPARC = 1.3267
