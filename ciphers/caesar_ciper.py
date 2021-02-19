alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar_cipher_encrypt(message, key):
    message = message.lower()
    ciphertext = ''
    for character in message:
        if character == ' ':
            ciphertext += character
        else:
            index = get_index(character)
            if index == -1:
                print("The character \'" + character + "\' in plaintext is not an english alphabet")
                return ""

            ciphertext += alphabets[(index + key) % 26]
    return ciphertext


def caesar_cipher_decrypt(ciphertext, key):
    ciphertext = ciphertext.lower()
    plaintext = ''
    for character in ciphertext:
        if character == ' ':
            plaintext += character
        else:
            index = get_index(character)
            if index == -1:
                print("The character \'" + character + "\' in ciphertext is not an english alphabet")
                return ""

            plaintext += alphabets[(index - key) % 26]
    return plaintext


def get_index(character):
    for i in range(len(alphabets)):
        if character == alphabets[i]:
            return i
    return -1

print("WELCOME TO CAESAR CIPHER")
option = input("Please select an option (Encrypt or Decrypt): ")
if option.lower() == "encrypt":
    plaintext = input("Enter the message to encrypt: ")
    key = input("Enter the key (integer): ")
    ciphertext = caesar_cipher_encrypt(plaintext, int(key))
    print("Ciphertext: " + ciphertext)
elif option.lower() == "decrypt":
    ciphertext = input("Enter the ciphertext to decrypt: ")
    key = input("Enter the key (integer): ")
    plaintext = caesar_cipher_decrypt(ciphertext, int(key))
    print("Plaintext: " + plaintext)
