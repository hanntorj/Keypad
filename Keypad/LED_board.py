import RPi.GPIO as GPIO
from time import sleep

pins = [18, 23, 24]

pin_led_states = [
[1, 0, -1],  # State A
[0, 1, -1],  # State B
[-1, 1, 0],  # State C
[-1, 0, 1],  # State D
[1, -1, 0],  # State E
[0, -1, 1]   # State F
]

GPIO.setmode(GPIO.BCM)


class LED_board:
    """charlieplexed LED board"""
    #def setup(self):
    #    '''set teh proper mode'''

    @staticmethod
    def set_pin(pin_index, pin_state):
        if pin_state == -1:
            GPIO.setup(pins[pin_index], GPIO.IN)
        else:
            GPIO.setup(pins[pin_index], GPIO.OUT)
            GPIO.output(pins[pin_index], pin_state)

    def light_single_led(self, led_number, light_time):
        """turn on one of 6 LED by making appropriate combo of I and O declarations, and making the appropriate
        HIGH/LOW  settings on O-pis """
        for pin_index, pin_state in enumerate(pin_led_states[led_number]):
            self.set_pin(pin_index, pin_state)
        sleep(light_time)

        self.set_pin(0, -1)
        self.set_pin(1, -1)
        self.set_pin(2, -1)

    def flash_all_leds(self):
        """Turns all leds on for a duration on 0,25 secs,then turn them off for a duration of 0,25 secs."""
        """One instance of flash_all_leds equal 0,5 seconds."""
        for pin in range(0, len(pins)):
            self.set_pin(pin, 1)
        sleep(0.25)
        for pin in range(0, len(pins)):
            self.set_pin(pin, -1)
        sleep(0.25)

    def twinkle_all_leds(self, duration): #Input duration in secs
        """Twinkles all LEDs for a given input duration, given in seconds. """
        for i in range(0, duration * 2):
            self.flash_all_leds()




        '''turn all LEDs on and off in sequence for k sec, k argument'''

    """define functions for lighting pattern powering on and off"""
