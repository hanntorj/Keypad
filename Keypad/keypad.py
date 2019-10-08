import RPi.GPIO as GPIO
class Keypad:
    '''Keypad'''
    def setup(self):
        '''Set the proper mode'''
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(18,GPIO.OUT)
        GPIO.setup(23,GPIO.OUT)
        GPIO.setup(24,GPIO.OUT)
        GPIO.setup(25,GPIO.OUT)
        GPIO.setup(17,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(27,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(22,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    def do_polling(self):
        '''use nested loops to determine the key currently being pressed on the keypad'''

    def get_next_signal(self):
        '''main interface between agent and keypad. initiate repeated calls to do_polling until a key press detected'''

