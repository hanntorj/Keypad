from Keypad import *
from FSM import *
from LED_board import *

class KPC:
    '''main method including variables'''


    def int_passcode_entry(self):
        '''clear passcode buffer and initiate a power up lighting sequence'''
    def get_next_signal(self):
        '''return the overrice-signal, if its non-blank. else query keypad for next pressed key'''
    def verify_login(self):
        '''check password. store as Y or N in the override-signal. call LED board for fail or pass lighting'''
    def validate_passcode_change(self):
        '''check if new password is legal. if so write to password file. password: 4 digits or more, only digits 0-9. call LED board for fail or pass lighting '''
    def light_one_led(self):
        '''Using values stored in the Lid and Ldur slots, call the LED Board and request that LED # Lid be turned on for Ldur seconds'''
    def flash_led(self):
        '''call LED board and request flashing og LEDs'''
    def twinkle_led(self):
        '''call LED board and request twinkling og LEDs'''
    def exit_action(self):
        '''call LED board to initiate power down LEDs'''
