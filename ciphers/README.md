----
Caesar Cipher
----
Caesar Cipher substitutes the alphabet with another alphabet. The key *k* in this, an integer, corresponds to the *k-th* alphabet in [a b c ... z]. 
#### Example:
    WELCOME TO CAESAR CIPHER
    Please select an option (Encrypt or Decrypt): encrypt
    Enter the message to encrypt: My name is Manveer Puri
    Enter the key (integer): 12
    Ciphertext: yk zmyq ue ymzhqqd bgdu

    Please select an option (Encrypt or Decrypt): decrypt
    Enter the ciphertext to decrypt: yk zmyq ue ymzhqqd bgdu
    Enter the key (integer): 12
    Plaintext: my name is manveer puri

----
Vigenère Cipher
----
Vigenère Cipher substitutes a different alphabet for every alphabet in the message based on the key. We repeat the key if the size of key is smaller than the size of the message. There are similarities between this cipher and Caesar cipher.
#### Example:
    WELCOME TO VIGENÈRE CIPHER
    Please select an option (Encrypt or Decrypt): encrypt
    Enter the message to encrypt: My name is Manveer Puri
    Enter the key: Phagwara
    Ciphertext: bf twmv xz swnmety vqrz

    Please select an option (Encrypt or Decrypt): decrypt
    Enter the ciphertext to decrypt: bf twmv xz swnmety vqrz
    Enter the key: Phagwara
    Plaintext: my name is manveer puri
