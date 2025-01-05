import json
import os
from cryptography.fernet import Fernet

KEY_FILE = "secret.key"


def generate_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as key_file:
            key_file.write(key)


def load_key():
    return open(KEY_FILE, "rb").read()


cipher = Fernet(load_key())


def save_data(data):
    encrypted_data = cipher.encrypt(json.dumps(data, indent=4).encode())
    with open("data.json", "wb") as data_file:
        data_file.write(encrypted_data)


