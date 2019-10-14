"""Klasse for keypad til prosjekt 5 - TDT4113"""

from time import sleep
import RPi.GPIO as GPIO

class Keypad:
    """Keypad"""

    def __init__(self):
        self.rows = [18, 23, 24, 25]
        self.cols = [17, 27, 22]
        self.keypad = [
            ["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"],
            ["*", "0", "#"]
        ]
        self.setup()

    def setup(self):
        """Set the proper mode"""
        GPIO.setmode(GPIO.BCM)
        for rowp in self.rows:
            GPIO.setup(rowp, GPIO.OUT)
        for colp in self.cols:
            GPIO.setup(colp, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def do_polling(self):
        """use nested loops to determine the key currently being pressed on the keypad"""
        row, col = -1, -1
        correct_input = True
        for rowp in self.rows:
            GPIO.output(rowp, GPIO.HIGH)
            for colp in self.cols:
                if GPIO.input(colp) == GPIO.HIGH:
                    row, col = rowp, colp
                    for _ in range(19):
                        sleep(10/1000)
                        if GPIO.input(colp) != GPIO.HIGH:
                            correct_input = False
                            break
                    if correct_input:
                        while GPIO.input(colp) == GPIO.HIGH:
                            sleep(2/1000)
                    else:
                        row, col = -1, -1
            GPIO.output(rowp, GPIO.LOW)
        return row, col

    def get_symbol(self, row, col):
        """
        Metode for å hente tegn basert på rad og kolonne
        :param row: int
        :param col: int
        :return: str
        """
        row_index = self.rows.index(row)
        col_index = self.cols.index(col)
        return self.keypad[row_index][col_index]

    def get_next_signal(self):
        """main interface between agent and keypad. initiate repeated calls to do_polling until a key press detected"""
        row, col = -1, -1
        while row == -1 and col == -1:
            row, col = self.do_polling()
            sleep(10/1000)
        return self.get_symbol(row, col)