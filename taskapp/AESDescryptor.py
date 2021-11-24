from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad


def decode(key, iv, ct):
    iv = iv.encode("utf-8")
    ct = b64decode(ct)
    key = key.encode("utf-8")
    cipher = AES.new(key, AES.MODE_CBC, iv)
    text = unpad(cipher.decrypt(ct), AES.block_size)
    # print("The message was: ", text)
    return {'text': text.decode("utf-8")}


