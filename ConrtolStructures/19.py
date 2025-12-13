###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = "The early bird catches the worm"
encrypted_text = ""

shift = 1

for char in plain_text:
    # read the character's code (use ord())
    char_code = ord(char)
    # add one to the character's code
    new_char_code = char_code + shift
    # replace new character code with its
    # corresponding character (use chr())
    encrypted_char = chr(new_char_code)
    # add encrypted character to encrypted text
    encrypted_text = encrypted_text + encrypted_char


print(f'Orginal text {plain_text}')
print(f'Cesar Code {encrypted_text}')
