# Practical 1
# implementing Ciphers

def encrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + s - 97) % 26 + 97)
        else:
            result += char
    return result

text = input("Enter the text to encrypt: ")
s = 3
print("Text : " + text)
print("Cipher: " + encrypt(text, s))
