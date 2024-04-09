# add your code here
plain_text = input("Please enter the Plain text: ")
plain_text = plain_text.lower()
cipher_text = ""
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
shifted_alphabet = ["f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e"]
for letter in plain_text:
    if letter in alphabet:
        cipher_text += shifted_alphabet[alphabet.index(letter)]
    else:
        cipher_text += letter
print("The Cipher text is", cipher_text)