import random
import string

class User(dict):
    def __init__(self, user_name, user_id, assigned_instruments):
        self.user_name = user_name
        self.user_id = user_id
        self.assigned_instruments = assigned_instruments

    def create_id(id_length=5):
        numbers = string.digits
        return ''.join(random.choice(numbers) for i in range(id_length))