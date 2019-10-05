
class Keypad:
    '''Keypad'''
    def setup(self):
        '''Set the proper mode'''
    def do_polling(self):
        '''use nested loops to determine the key currently being pressed on the keypad'''
    def get_next_signal(self):
        '''main interface between agent and keypad. initiate repeated calls to do_polling until a key press detected'''
