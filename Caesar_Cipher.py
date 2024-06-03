logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
 
           88             88                                 
           88             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text,shift,direction):

    code=''
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            if direction == 'encode':
                new_position = (position + shift) % 26
            elif direction == 'decode':
                new_position = (position - shift) % 26
            else:
                print("Invalid direction. Please choose 'encode' or 'decode'.")
                return
            new_letter = alphabet[new_position]
            code += new_letter
        else:
            code += char

    print(f"The {direction}d result: {code}")

while True:
    code_direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    cipher_text = input("Type your message:\n").lower()
    cipher_shift = int(input("Type the shift number:\n"))

    caesar(cipher_text,cipher_shift,code_direction)

    continuation=input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if continuation == "no":
        print("See you again!\n")
        break
