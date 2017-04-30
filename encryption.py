import base64

def encode(key, clear):          # key -> password, clear -> will be encrypted
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.b64encode("".join(enc))   # returns incrypted string

def decode(key, enc):            # key -> password, enc -> will be decrypted
    dec = []
    enc = base64.b64decode(enc)
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)         # returns decrypted string

key="afgd"                      # serves as password.
string="razdvatri"              # the string will be encrypted and decrypted.
ENC = encode(key, string)
print ENC
DEC = decode(key, ENC)
print DEC


