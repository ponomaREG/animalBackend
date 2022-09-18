import random
from app import app

class Token:

    @staticmethod
    def generateToken():
        length = app.config["TOKEN_LENGTH"]
        symbols = app.config["AVAILABLE_SYMBOLS"]
        return ''.join(random.choice(symbols) for i in range(length))
