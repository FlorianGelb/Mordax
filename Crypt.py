from Crypto import Random
from Crypto.Random import random
from Crypto.Cipher import AES
import hashlib
import string
import base64, sys
class Crypt():

    def KeyAndIv(self, key, iv):
        Letters = list (string.ascii_letters)
        if iv != 0:
            self.iv = iv
        else:
            self.iv =""
            for x in range (16):
                self.iv = self.iv + random.choice(Letters)
        self.key = hashlib.sha256(str.encode(key))
        return self.iv

    def pad(self, msg):
        while len(msg)%16 != 0:
            msg = msg + "*"
        return msg

    def encode(self, msg):
        msg = self.pad(msg)
        cipher = AES.new(self.key.digest(), AES.MODE_CBC, self.iv)
        cipher = cipher.encrypt(msg)
        return(cipher)

    def decode(self, msg):
        msg = self.pad(msg)
        cipher = AES.new(self.key.digest(), AES.MODE_CBC, self.iv)
        return cipher.decrypt(msg)

    depad = lambda self, msg: msg.rstrip("*")
    b64Enc = lambda self, msg: base64.b64encode(self.encode(msg))
    b64Dec = lambda self, msg: self.depad(self.decode(base64.b64decode(msg)))

