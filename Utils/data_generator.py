import random
import string
import time

def generate_email():
    return f"test{int(time.time())}@mail.com"

def generate_phone():
    return "9" + "".join(random.choices(string.digits, k=9))

def generate_string(length=6):
    return "".join(random.choices(string.ascii_letters, k=length))