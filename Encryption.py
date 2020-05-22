"""
Requirements:
1. Accept a string input
2. Add in random letter in every other index position
3. Reverse the string
4. Create a shuffle version of the alphabet
5. Match index of each letter and encrypt the letter using the shuffled alphabet
6. Create a Decryption Script if provided with the seed key.
"""
import string
import random

class Encryption():
    
    #Create string
    alphastring = string.ascii_lowercase
    
    #initialize object and holding the original info
    def __init__(self, encrypt_info, seed):
        self.encrypt_info = encrypt_info
        self.seed = seed
        self.alphaindex = list(range(0,25))

        #Intialize empty list to hold encryption info
        self.encryption_string = []
    

    def encode(self):
        random.seed(self.seed)


        #initiali step to add random characters after every char
        for char in self.encrypt_info.lower():
            
            self.encryption_string.append(char)

            x = random.randint(0,25)
            self.encryption_string.append(self.alphastring[x])

        print("Add Random Chars {}".format(self.encryption_string))

        #Reverse the string
        self.encryption_string.reverse()

        print("\nReverse chars {}".format(self.encryption_string))

        random.seed(self.seed)

        #shuffle index
        random.shuffle(self.alphaindex)

        print("\nAlpha Index: {}".format(self.alphaindex))
        
        cipher_code = []

        for pos in self.alphaindex:
            cipher_code.append(self.alphastring[pos])

        print("\nCipher Code: {}".format(cipher_code))
        self.final_encryption = []

        print(list(self.encryption_string))
        for char in self.encryption_string:
            if char in self.alphastring:
                self.index_pos = self.alphastring.index(char)
                self.final_encryption.append(cipher_code[self.index_pos])
            else:
                self.final_encryption.append(char)

        return "".join(self.final_encryption)

class Decryption():
    alphastring = string.ascii_lowercase
    

    def __init__ (self, message, seed):
        self.message = message
        self.seed = seed
        self.alphaindex = list(range(0,25))

    def decrypt_message(self):
        random.seed(self.seed)

        print("\nOriginal Encrypted Message: {}".format(self.message))

        random.shuffle(self.alphaindex)
        
        print("\n Alpha Index: {}".format(self.alphaindex))

        self.cipher_code = []

        for pos in self.alphaindex:
            self.cipher_code.append(self.alphastring[pos])

        print("Decrypt Cypher Code: {}".format(self.cipher_code))
        
        self.reverse_encryption = []

        print(list(self.message))
        for char in self.message:
            if char in self.cipher_code:
                self.index_pos = self.cipher_code.index(char)
                self.reverse_encryption.append(self.alphastring[self.index_pos])
            else:
                self.reverse_encryption.append(char)

        print("\nReversed Message: {}".format("".join(self.reverse_encryption)))

        self.reverse_encryption.reverse()

        print("\nOriginal Message with extra chars: {}".format("".join(self.reverse_encryption)))

        self.decrypted_message = []
        for i, char in enumerate(self.reverse_encryption):
            if i == 0:
                self.decrypted_message.append(char)
            elif i % 2 != 0:
                pass
            else:
                self.decrypted_message.append(char)

        return "".join(self.decrypted_message)
    








##data = input("Input your Message: ")
##seed_value = input("Input your seed value: ")
data = "Hello World"
seed_value = 40

enc = Encryption(data, int(seed_value))

result = enc.encode()

print("\nEncrypted Message Result: {}".format(result) )

print("\nNow Decrypting Message")

dec = Decryption(result, int(seed_value))

decrypt_message = dec.decrypt_message()
print("\nDecrypted Message: {}".format(decrypt_message))

