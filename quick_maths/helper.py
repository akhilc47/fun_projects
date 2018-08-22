import random


def get_puzzle():
    operator = random.choice(['+', '+', '-', '*', '*', '/']) # Twice as likely to get addition or multiplication

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

    return '%d %s %d' % (arg1, operator, arg2), answer
