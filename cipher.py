# add your code here
encription_dict = {"a":"f", "b":"g", "c":"h", "d":"i", "e":"j", "f":"k", "g":"l", "h":"m", "i":"n", "j":"o", "k":"p", "l":"q", "m":"r", "n":"s",  "o":"t", "p":"u", "q":"v", "r":"w", "s":"x", "t":"y", "u":"z", "v":"a", "w":"b", "x":"c", "y":"d", "z":"e"}


text = input("Enter message:")
text = text.lower()
secret = ""
for word in text:
    secret += encription_dict.get(word, word)
print(secret)