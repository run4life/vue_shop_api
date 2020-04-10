
import base64

def encrypt(string):
    newstring = base64.b64encode(string)
    return newstring

def decrypt(string):
    newstring = base64.b64decode(string)
    return newstring