from Keypad import *
from FSM import *


# from LED_board import *


class KPC:
    """main method including variables"""

    def __init__(self):
        self.keypad = Keypad()
        self.LED = LED_board()
        self.passcode_buffer = ''
        self.path_password = 'password.txt'
        self.override_signal = None
        self.password = ''
        self.LED_id = ''
        self.LED_duration = ''
        self.new_pass = ''
        self.new_pass_check = ''
        f = open(self.path_password)
        try:
            self.password = f.read().strip()
        except IOError:
            print("Could not set password")
        finally:
            f.close()

    def int_passcode_entry(self):
        """clear passcode buffer and initiate a power up lighting sequence"""
        self.passcode_buffer = ''
        # TODO fiks LEDs tel å match power-up sequence

    def get_next_signal(self):
        """return the overrice-signal, if its non-blank. else query keypad for next pressed key"""

    def verify_login(self):
        """check password. store as Y or N in the override-signal. call LED board for fail or pass lighting"""

    def validate_passcode_change(self):
        """check if new password is legal. if so write to password file.
        Password: 4 digits or more, only digits 0-9. call LED board for fail or pass lighting """
        # Tre rød LEDs for fail og tre grønne for pass?
        if self.new_pass == self.new_pass_check:
            self.password = self.new_pass
            # TODO twinkle LEDs for passing
        else:
            # TODO twinkle LEDs for failing
            self.LED.twinkle
        self.new_pass = ''
        self.new_pass_check = ''

    def light_one_led(self):
        """Using values stored in the Lid and Ldur slots, call the LED Board and request that LED # Lid be turned on
        for Ldur seconds """
        self.LED.light_single_led(int(self.LED_id), self.LED_duration)  # Usikker på om LED_id må castes til int

    def flash_led(self):
        """call LED board and request flashing og LEDs"""
        self.LED.flash_all_leds

    def twinkle_led(self):
        """call LED board and request twinkling og LEDs"""
        self.LED.twinkle_all_leds(self.LED_duration)

    def exit_action(self):
        """call LED board to initiate power down LEDs"""
        # Lagrer passord i filen når keypad-en slås av
        f = open(self.path_password, "w")
        try:
            self.password
        except IOError:
            print("Couldn't save password in respective file")
        finally:
            f.close()
        # TODO twinkle LEDs to signal powering down
