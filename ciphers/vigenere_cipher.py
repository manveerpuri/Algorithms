alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def vigenère_cipher_encrypt(message, key):
    message = message.lower()
    key = key.lower()
    ciphertext = ''
    for i in range(len(message)):
        character = message[i]
        key_character = key[i % len(key)]
        if character == ' ':
            ciphertext += character
        else:
            index = get_index(character)
            key_index = get_index(key_character)

            if index == -1:
                print("The character \'" + character + "\' in plaintext is not an english alphabet")
                return ""

            ciphertext += alphabets[(index + key_index) % 26]
    return ciphertext


def vigenère_cipher_decrypt(ciphertext, key):
    ciphertext = ciphertext.lower()
    key = key.lower()

    plaintext = ''
    for i in range(len(ciphertext)):
        character = ciphertext[i]
        key_character = key[i % len(key)]

        if character == ' ':
            plaintext += character
        else:
            index = get_index(character)
            key_index = get_index(key_character)

            if index == -1:
                print("The character \'" + character + "\' in ciphertext is not an english alphabet")
                return ""

            plaintext += alphabets[(index - key_index) % 26]
    return plaintext


def get_index(character):
    for i in range(len(alphabets)):
        if character == alphabets[i]:
            return i
    return -1

print("WELCOME TO VIGENÈRE CIPHER")
option = input("Please select an option (Encrypt or Decrypt): ")
if option.lower() == "encrypt":
    plaintext = input("Enter the message to encrypt: ")
    key = input("Enter the key: ")
    ciphertext = vigenère_cipher_encrypt(plaintext, key)
    print("Ciphertext: " + ciphertext)
elif option.lower() == "decrypt":
    ciphertext = input("Enter the ciphertext to decrypt: ")
    key = input("Enter the key: ")
    plaintext = vigenère_cipher_decrypt(ciphertext, key)
    print("Plaintext: " + plaintext)
