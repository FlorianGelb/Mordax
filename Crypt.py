from Crypto.Random import random
from Crypto.Cipher import AES
import hashlib
import string
import base64


class Crypt:
    def __init__(self):
        self.initialization_vector = 0
        self.key = 0

    def key_and_iv(self, key, iv):
        letters = list(string.ascii_letters)
        if iv != 0:
            self.initialization_vector = iv
        else:
            self.initialization_vector = ""

            for x in range(16):

                self.initialization_vector = self.initialization_vector + random.choice(letters)

        self.key = hashlib.sha256(str.encode(key))
        return self.initialization_vector

    def pad(self, msg):
        while len(msg) % 16 != 0:
            msg = msg + "*"
        return msg

    def encode(self, msg):
        msg = self.pad(msg)
        cipher = AES.new(self.key.digest(), AES.MODE_CBC, self.initialization_vector)
        cipher = cipher.encrypt(msg)
        return cipher

    def decode(self, msg):
        msg = self.pad(msg)
        cipher = AES.new(self.key.digest(), AES.MODE_CBC, self.initialization_vector)
        return cipher.decrypt(msg)

    depad = lambda self, msg: msg.rstrip("*")
    b64Enc = lambda self, msg: base64.b64encode(self.encode(msg))
    b64Dec = lambda self, msg: self.depad(self.decode(base64.b64decode(msg)))
    gitb64 = lambda self, txt: base64.b64decode(txt)
