import sys
import base64

def encrypt(plaintext, key):
    ciphertext = ''
    key = key if isinstance(key, list) else [key]
    key_length = len(key)
    for i in range(len(plaintext)):
        character = plaintext[i]
        codepoint = ord(character)
        key_value = key[i % key_length]
        if codepoint + key_value > sys.maxunicode:
            raise ValueError('codepoint + key_value > sys.maxunicode')
        target = codepoint + key_value
        ciphertext += chr(target)
    # print('Ciphertext:\n%s\n' %ciphertext)
    bytearr = ciphertext.encode('utf-8')
    encoded_ciphertext = base64.b64encode(bytearr).decode('utf-8')
    return encoded_ciphertext

def decrypt(ciphertext, key):
    plaintext = ''
    decoded_ciphertext = base64.b64decode(ciphertext).decode('utf-8')
    key = key if isinstance(key, list) else [key]
    key_length = len(key)
    for i in range(len(decoded_ciphertext)):
        character = decoded_ciphertext[i]
        codepoint = ord(character)
        key_value = key[i % key_length]
        if codepoint - key_value < 0:
            raise ValueError('codepoint - key < 0')
        source = codepoint - key_value
        plaintext += chr(source)
    return plaintext

if __name__ == '__main__':
    message = 'hello world! it is thursday july 9 2026'
    key = [235, 237, 301, 317]
    print('Message:\n%s\n' %message)
    encrypted_message = encrypt(message, key)
    print('Encrypted message:\n%s\n' %encrypted_message)
    decrypted_message = decrypt(encrypted_message, key)
    print('Decrypted message:\n%s' %decrypted_message)
