import math
import time
from machine import ADC

class MQ(object):
    """
    Base class for dealing with MQ gas sensors. 
    Based on MQ135 MicroPython code written by rubfi: https://github.com/rubfi/MQ135

    TODO: logarithmic ppm calculation
    """

    # Assumed load resistance of the sensor
    RLOAD = None

    #Calibration resistance
    RZERO = None

    #Params for calculating ppm
    PPMPARA = None
    PPMPARB = None

    #Params for calculating temperature and humidity correction
    THPARA = None
    THPARB = None
    THPARC = None

    def __init__(self, pin):
        self.pin = pin

    def get_resistance(self):
        """Returns the resistance of the sensor in kOhms // -1 if not value got in pin"""
        adc = ADC(self.pin)
        value = adc.read()
        if value == 0:
            return -1
        
        return (1023./value - 1.) * self.RLOAD
    
    def get_correction_factor(self, temperature, humidity):
        """Returns correction factor for current temperature and humidity, based on curves, provided in the datasheet"""
        return self.THPARA * temperature + (self.THPARB * humidity + self.THPARC)

    def get_corrected_resistance(self, temperature, humidity):
        """Gets the resistance of the sensor corrected for temperature/humidity"""
        return self.get_resistance()/ self.get_correction_factor(temperature, humidity)

    def get_ppm(self):
        """Returns the ppm of measured component"""
        return self.PPMPARA * math.pow((self.get_resistance() / self.RZERO), self.PPMPARB)

    def get_corrected_ppm(self, temperature, humidity):
        """Returns the ppm of H2S corrected to temp/humidity"""
        return self.PPMPARA * math.pow((self.get_corrected_resistance(temperature, humidity) / self.RZERO), self.PPMPARB)