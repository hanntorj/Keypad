from LED_board import LED_board
from keypad import Keypad

hanna tester

class KPC:
    """main method including variables"""

    def __init__(self):
        """Initialiser, setting the initializer"""
        self.keypad = Keypad()
        self.LED = LED_board()
        self.passcode_buffer = ''
        self.digit = ''
        self.path_password = 'password.txt'
        self.override_signal = ''
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

    def init_passcode_entry(self):
        """clear passcode buffer and initiate a power up lighting sequence"""
        self.passcode_buffer = ''
        self.LED.led_power_up()

    def get_next_signal(self):
        """return the override-signal, if its non-blank. else query keypad for next pressed key"""
        if self.override_signal != '':
            return self.override_signal
        self.digit = self.keypad.get_next_signal()
        return self.digit

    def append_password_buffer(self):
        """Appends password with newly pressed digit"""
        self.password_buffer += self.digit

    def append_new_pass(self):
        """Appends password with newly pressed digit"""
        self.new_pass += self.digit
        self.digit = ''

    def append_new_pass_check(self):
        """Appends password with newly pressed digit"""
        self.new_pass_check += self.digit
        self.digit = ''

    def append_Ldur(self):
        """Appends digit to time-variable"""
        self.LED_duration += self.digit

    def set_led(self):
        """Sets the Lpin"""
        self.LED_id = self.digit

    def verify_login(self):
        """Checks the password. store as Y or N(Yes or No) in the override-signal. call LED board for fail or pass lighting"""
        if self.passcode_buffer == self.password:
            self.override_signal = 'Y'
            self.LED.led_login_successful()
            print('correct password')
        else:
            self.override_signal = 'N'
        self.password_buffer = ''

    def validate_passcode_change(self):  # ikke fullført
        """check if new password is legal. if so write to password file.
        Password: 4 digits or more, only digits 0-9. call LED board for fail or pass lighting """
        # Tre rød LEDs for fail og tre grønne for pass?
        if self.new_pass == self.new_pass_check:
            self.password = self.new_pass
            self.LED.led_pass_change_successful()
        else:
            self.LED.led_pass_change_unsuccessful()
        self.new_pass = ''
        self.new_pass_check = ''

    def set_password(self):
        """stores new password in password file"""
        # må vi slette passordet på begynnelsen?
        with open(self.path_password, 'w') as file:
            file.write(self.password)

    def light_one_led(self):  # trenger vi denne?????
        """Using values stored in the Lid and Ldur slots, call the LED Board and request that LED # Lid be turned on
        for Ldur seconds """
        self.LED.light_single_led(
            int(self.LED_id), self.LED_duration)  # Usikker på om LED_id må castes til int

    def flash_led(self):
        """call LED board and request flashing og LEDs"""
        self.LED.flash_all_leds()

    def twinkle_led(self):
        """call LED board and request twinkling og LEDs"""
        self.LED.twinkle_all_leds(self.LED_duration)

    def reset_all_variables(self):
        self.passcode_buffer = ''
        self.override_signal = None
        self.new_pass = ''
        self.new_pass_check = ''
        self.LED_id = ''
        self.LED_duration = ''

    def power_down(self):  # hanna skjønner ikke helt denne her
        """Close file and call LED board to initiate power down LEDs"""
        # Lagrer passord i filen når keypad-en slås av
        f = open(self.path_password, "w")
        try:
            self.password
        except IOError:
            print("Couldn't save password in respective file")
        finally:
            f.close()
        self.LED.led_power_down()

    def nothing(self):
        pass
