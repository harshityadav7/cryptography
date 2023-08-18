from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_ECB)


def encrypt(plaintext):
    padded_plaintext = pad(plaintext.encode(), AES.block_size)
    ciphertext = cipher.encrypt(padded_plaintext)
    return ciphertext


def decrypt(ciphertext):
    padded_plaintext = cipher.decrypt(ciphertext)
    plaintext = unpad(padded_plaintext, AES.block_size)
    return plaintext.decode()


plaintext = input("enter the text")
print("Plaintext:", plaintext)
encrypted_text = encrypt(plaintext)
print("Encrypted text:", encrypted_text)
x=input("do you want to decrypt...y/n? ")
if x=='y' or x=='Y':
    decrypted_text = decrypt(encrypted_text)
    print("Decrypted text:", decrypted_text)
else:
    print("end")


