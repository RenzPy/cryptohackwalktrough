from pwn import xor

# Given string "label" and XOR with 13
original_string = "label"
key = 13

# Perform XOR operation
encrypted_string = xor(original_string, key)

# Wrap the encrypted string with "crypto{" and "}" to create the flag
flag = f"crypto{{{encrypted_string}}}"
print(flag)
