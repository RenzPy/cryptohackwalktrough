import base64

# QUESTION HEX STRING 
string = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'
# DECODE FROM HEX TO BYTES
htoby = bytes.fromhex(string)
# DECODE FROM BYTES TO BASE64
bytob64 = base64.b64encode(htoby)

# DECODE FROM B64 TO STRINGS & PRINT
solution = base64.b64decode(bytob64)
print(bytob64)
list