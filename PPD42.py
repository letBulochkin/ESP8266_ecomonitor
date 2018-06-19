import utime
import math
from machine import Pin

class PPD42(object):
    """
    Micropython library to deal with Shinyei PPD42 Dust Sensor.
    Based on calculating dust concentration by measuring Low Pulse Occupance of sensor's output signal.

    TODO: add constants.
    """

    def __init__(self, pin):
        self.pin = pin

    def get_concentration(self):
        """
        Calculate PM concentration from LPO ratio.
        Based on datasheet curve.

        Returns concentration in particles per cubic feet or smth similar, whatever. 

        TODO: Rewrite to calculate concentration in normal terms.
        """

        ratio = self.get_LPO()
        return 1.1 * math.pow(ratio, 3) - 3.8 * math.pow(ratio, 2) + 520 * ratio + 0.62

    def get_LPO(self):
        """
        Calculates LPO (Low Pulse Occupance) ratio to the detecting interval

        Returns percentage of LPO.
        """

        time_intervals = self.get_times()
        return float(sum((i * math.pow(10, -6) for i in time_intervals))) / float(30) * 100.0 

    def get_times(self):
        """
        Calculates amount of time, during which LOW signal is recieved by pin.
        Calculations are made on 30-second period.

        Returns list of time intervals in microseconds. 
        """

        Times = []
        time_passed = 0
        # print("Start!")
        start = utime.time()

        while time_passed < 31:
            if self.pin.value() == 0:
                t1 = utime.ticks_us()
                
                while self.pin.value() == 0:
                    # print(p5.value())
                    pass
                
                t2 = utime.ticks_us()
                Times.append(utime.ticks_diff(t2,t1))
            
            time_passed = utime.time() - start
        
        # print(type(Times))
        # print(len(Times))
        # print(*Times, sep = "\n")

        return Times

'''
def calc():
    Times = []
    time_passed = 0
    print("Start!")
    start = utime.time()

    while time_passed < 31:
        if p5.value() == 0:
            t1 = utime.ticks_us()
            while p5.value() == 0:
                print(p5.value())
                pass
            t2 = utime.ticks_us()
            Times.append(utime.ticks_diff(t2,t1))
        time_passed = utime.time() - start
    
    #print(type(Times))
    #print(len(Times))
    #print(*Times, sep = "\n")

    return Times
'''

if __name__ == "__main__":
    
    p5 = Pin(5, Pin.IN)
    t = []
    utime.sleep(2)
    print("Engage!")
    # calc()



