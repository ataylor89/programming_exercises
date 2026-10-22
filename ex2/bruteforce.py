from addsubtract2 import decrypt

threshold = 3

with open('dictionary.txt', 'r') as file:
    dictionary = [line.strip() for line in file]

with open('encrypted_message.txt', 'r') as file:
    encrypted_message = file.read()

success = False
try:
    for key in range(0, 0x88000):
        message = decrypt(encrypted_message, key)
        tokens = [token.lower() for token in message.split()]
        intersection = list(set(dictionary) & set(tokens))
        if len(intersection) > threshold:
            success = True
            print('Success! We were able to decrypt the encrypted message.')
            print(f'Message: {message}')
            print(f'Key: {key}')
except ValueError:
    pass
except Exception as e:
    print(repr(e))

if not success:
    print('We were unable to decrypt the encrypted message.')
