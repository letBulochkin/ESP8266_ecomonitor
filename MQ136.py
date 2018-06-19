import math
import time
from machine import ADC

class MQ136(object):
    # Assumed load resistance of the board
    RLOAD = 10.0

    #Calibration resistance, calculated assuming 10 ppm of H2S in the air
    RZERO = 0.0000005638

    #Params for calculating H2S ppm
    PPMPARA = 0.5907
    PPMPARB = -0.2675

    #Params for calculating temperature and humidity correction
    THPARA = -0.014
    THPARB = -0.0076
    THPARC = 1.812

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
        return self.THPARA * temperature + (self.THPARB * humidity + self.THPARC)

    def get_corrected_resistance(self, temperature, humidity):
        """Gets the resistance of the sensor corrected for temperature/humidity"""
        return self.get_resistance()/ self.get_correction_factor(temperature, humidity)

    def get_ppm(self):
        """Returns the ppm of H2S"""
        return self.PPMPARA * math.pow((self.get_resistance() / self.RZERO), self.PPMPARB)

    def get_corrected_ppm(self, temperature, humidity):
        """Returns the ppm of H2S corrected to temp/humidity"""
        return self.PPMPARA * math.pow((self.get_corrected_resistance(temperature, humidity) / self.RZERO), self.PPMPARB)



