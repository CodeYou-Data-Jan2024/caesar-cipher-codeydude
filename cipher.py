# add your code here
plaintext = input("Please enter a sentence: ").lower()
encrypted_text = ""
for char in plaintext:
    char_to_ascii = ord(char)
    if  97 <= char_to_ascii <= 122:
        char_to_ascii += 5
        if char_to_ascii > 122:
            diff = char_to_ascii - 122
            if diff == 1:
                char_to_ascii = 97
            elif diff == 2:
                char_to_ascii = 98
            elif diff == 3:
                char_to_ascii = 99
            elif diff == 4:
                char_to_ascii = 100
            elif diff == 5:
                char_to_ascii = 101
    encrypted_text = encrypted_text + chr(char_to_ascii)
print("The encrypted sentences is:", encrypted_text)