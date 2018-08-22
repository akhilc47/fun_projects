import configparser
import random
from collections import defaultdict


class QuickMathGame:
    def __init__(self):
        self.answer = 0
        self.game_running = False
        self.players = defaultdict(lambda: 0, {})
        self.question, self.answer = '', 0
        self.get_puzzle()

    def get_puzzle(self):
        """
        Creates a math question which has a single, basic operation.
        :return: returns a string (in the format <arg1> <operator> <arg2>) and an int which is the answer
        """
        operator = random.choice(['+', '+', '-', '*', '*', '/'])  # Twice as likely to get addition or multiplication

        if operator == '+':
            arg1 = random.randint(0, 99)
            arg2 = random.randint(0, 99)
            answer = arg1+arg2

        elif operator == '-':
            arg1 = random.randint(0, 99)
            arg2 = random.randint(0, arg1)
            answer = arg1-arg2

        elif operator == '*':
            arg1 = random.randint(0, 50)
            arg2 = random.randint(0, 10)
            answer = arg1*arg2

        else:
            arg1 = random.randint(0, 20)
            arg2 = random.randint(1, arg1)
            answer = arg1*arg2
            arg1, answer = answer, arg1

        self.question, self.answer = '%d %s %d' % (arg1, operator, arg2), answer


def get_token():
    """
    Reads the token stored in "config.ini"
    :return:
    """
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['REMOTE']['token']
