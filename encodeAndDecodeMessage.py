alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

print("write number please then press enter:")
key = int(input())

def encode(letter, key):
    pos = alphabet.find(letter)
    newpos = (pos + key)
    if newpos >= 26:
        newpos = newpos - 26
    return alphabet[newpos]

def decode(letter, key):
    pos = alphabet.find(letter)
    newpos = (pos - key)
    if newpos < 0:
        newpos = newpos + 26
    return alphabet[newpos]

print("write the message you want to encode:")
message = input()
output = ""
for character in message:
    if character in alphabet:
        output = output + encode(character, key)
    else:
        output = output + character

print("encoded message:", output)

print("write the message you want to decode:")
message1 = input()
output = ""
for character in message1:
    if character in alphabet:
        output = output + decode(character, key)
    else:
        output = output + character
print("decoded message:", output)