import time

class ShiftRegisters:
    def __init__(self, **kwargs):
        '''
        Initialise the ShiftRegisters.

        Parameters
        ----------
        All parameters are keyword parameters.

        set_output
            should be a function that takes a pin number and a level (False/True)
            and sets the pin to the level
        ser : int
            should be the pin connected to SER
        srclk : int
            should be the pin connected to SRCLK
        rclk : int
            should be the pin connected to RCLK
        srclk_delay : float
            ... in ms
        num_registers : int, optional
            ... (default: 1)
        initial : set, optional
            if provided, set pins in set to high, all other pins to low
        '''
        self.set_output = kwargs.get('set_output')
        if self.set_output is None:
            raise ValueError('set_output function is missing')

        self.ser_pin = kwargs.get('ser')
        if self.ser_pin is None:
            raise ValueError('ser pin number is missing')

        self.srclk_pin = kwargs.get('srclk')
        if self.srclk_pin is None:
            raise ValueError('srclk pin number is missing')

        self.rclk_pin = kwargs.get('rclk')
        if self.rclk_pin is None:
            raise ValueError('rclk pin number is missing')

        self.srclk_delay = kwargs.get('srclk_delay')
        if self.srclk_delay is None:
            raise ValueError('srclk_delay is missing')

        self.num_registers = kwargs.get('num_registers', 1)

        initial = kwargs.get('initial')
        if initial is not None:
            self.set_all(initial)

    def set_all(self, pins):
        pins = set(pins)
        self.set_output(self.rclk_pin, False)
        for pin in range(self.num_registers * 8 - 1, -1, -1):
            self.set_output(self.srclk_pin, False)
            if pin in pins:
                self.set_output(self.ser_pin, True)
            else:
                self.set_output(self.ser_pin, False)
            self.set_output(self.srclk_pin, True)
            time.sleep(float(self.srclk_delay) / 1000)
        self.set_output(self.rclk_pin, True)
