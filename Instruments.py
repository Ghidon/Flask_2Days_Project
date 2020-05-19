import random
import string


class Instruments(dict):
    def __init__(self, instrument_name, instrument_id):
        self.instrument_name = instrument_name
        self.instrument_id = instrument_id

    def create_id(id_length=5):
        numbers = string.digits
        return ''.join(random.choice(numbers) for i in range(id_length))
