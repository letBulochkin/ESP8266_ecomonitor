from machine import Pin

class Multiplexor(object):
    """
    Micropython library to deal with multiplexors.
    Toggle pin: pin that switches on or off multiplexor.
    Control pins: digital pins, that control input/output connection
    Toggle pin may be None if you don't use it. 
    """

    def __init__(self, toggle_pin, *pins):
        self.toggle_pin = Pin(toggle_pin, Pin.OUT)
        self.control_pins = [Pin(x, Pin.OUT) for x in pins]

    def switch(self, channel):
        """Switches between input channels"""
        for i in range(len(self.control_pins)):
            self.control_pins[i].value(0)  # set all pins to LOW
        channel = "{0:b}".format(channel - 1)  # format channel number to binary, assuming channels start from 1 
        for i in range(len(channel)):
            try:
                self.control_pins[len(self.control_pins) - len(channel) + i].value(int(channel[i]))  # set control pin value
            except Exception as e:
                raise ValueError("Channel is out of provided pin range") from e 

    def toggle(self):
        """Turns multiplexor on or off"""
        if self.toggle_pin == None:
            raise ValueError("Toggle pin was not provided")
        else:
            self.toggle_pin.value(1 - self.toggle_pin.value())  # invert control pin value
