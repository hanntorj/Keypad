import RPi.GPIO as GPIO
from time import sleep, time


class LED_board:
    """charlieplexed LED board"""
    # def setup(self):
    #    '''set the proper mode'''

    def __init__(self):
        self.pins = [4, 5, 12]
        self.pin_led_states = [
            [1, 0, -1],  # State A
            [0, 1, -1],  # State B
            [-1, 1, 0],  # State C
            [-1, 0, 1],  # State D
            [1, -1, 0],  # State E
            [0, -1, 1]  # State F
        ]
        GPIO.setmode(GPIO.BCM)

    def set_pin(self, pin_index, pin_state):
        """Method for setting the pins"""
        if pin_state == -1:
            GPIO.setup(self.pins[pin_index], GPIO.IN)
        else:
            GPIO.setup(self.pins[pin_index], GPIO.OUT)
            GPIO.output(self.pins[pin_index], pin_state)

    def light_single_led(self, led_number, duration=0.5):
        """Turn on the given led with an optional argument of time, and turn it off again."""
        for pin_index, pin_state in enumerate(self.pin_led_states[led_number]):
            self.set_pin(pin_index, pin_state)
        sleep(duration)
        self.led_reset()

    def flash_all_leds(self, duration):
        """Flashes all leds on and off for argument "duration" amount of seconds.
        Time() returns the current time in seconds """
        stop_time = time() + duration
        while time() <= stop_time:
            for led_index in range(0, len(self.pin_led_states)):
                self.light_single_led(led_index, 0.2)

    def twinkle_all_leds(self, duration):  # Input duration in secs
        """Twinkles all leds in a interweaving pattern for the given duration"""
        stop_time = time() + duration
        while time() <= stop_time:
            for led_index in range(0, 6, 2):
                self.light_single_led(led_index, 0.2)
            for led_index in range(1, 6, 2):
                self.light_single_led(led_index, 0.2)

    def led_login_unsuccessful(self):
        """Led pattern that should show when an unsuccessful login attempt is made"""
        self.flash_all_leds(2)

    def led_login_successful(self):
        """Led pattern that should show when a successful login attempt is made"""
        self.twinkle_all_leds(2)

    def led_power_down(self):
        """Led pattern that should show when system is powering down"""
        stop_time = time() + 2
        while time() <= stop_time:
            self.light_single_led(1, 0.2)
            self.light_single_led(2, 0.2)
            self.light_single_led(3, 0.2)

    def led_power_up(self):
        """Led pattern that should show when system is powering up"""
        stop_time = time() + 2
        while time() <= stop_time:
            self.light_single_led(4, 0.2)
            self.light_single_led(5, 0.2)
            self.light_single_led(6, 0.2)

    def led_pass_change_successful(self):
        self.twinkle_all_leds(1)
        self.flash_all_leds(1)

    def led_pass_change_unsuccessful(self):
        stop_time = time() + 2
        while time() <= stop_time:
            self.light_single_led(5, 0.1)
            self.light_single_led(6, 0.1)

    def led_reset(self):
        """Assisting method for resetting the pins to an "off" state"""
        for led_number in range(0, 3):
            self.set_pin(led_number, -1)