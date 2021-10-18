
#Notes (what I learned from this):
# self is a placeholder for the name of the object
# self.var ==> attribute of self
# self.funct() ==> is a method of self
# strings are immutable 

class encryption:
    def __init__(self,text,ciphertext):
        self.text = text
        self.ciphertext = ciphertext

    def caesar(self,key):
        for i in self.text:
            temp = ord(i)
            if (temp >= 97 and temp <= 122):
                temp = temp - 97
                temp = 97 + (temp+int(key)) % 26 
                self.ciphertext += chr(temp)
            elif(temp >= 64 and temp <= 90):
                temp = temp - 65
                temp = 65 + (temp+int(key)) % 26 
                self.ciphertext += chr(temp)
            else:
                self.ciphertext += i

    def decaesar(self,key):
        for i in self.text:
            temp = ord(i)
            if (temp >= 97 and temp <= 122):
                temp = temp - 97
                temp = 97 + (temp - int(key)) % 26 
                self.ciphertext += chr(temp)
            elif(temp >= 65 and temp <= 90):
                temp = temp - 65
                temp = 65 + (temp-int(key)) % 26 
                self.ciphertext += chr(temp)
            else:
                self.ciphertext += i
      
    def vigenere(self,key):
        #I apologise to my future self for the magic numbers and weird variables.
        j = 0 #j is an increment variable that keeps track of where in the key the current iteration of the loop is at. It is used to find modularj that cycles through the key for every letter.
        key = key.upper()
        for i in self.text:
            modularj = j % len(key) #if j > length ==> modularj = j % len(self.text) if j < length ==> modularj = j % len(key-1)
            temp = ord(i)          
            if (temp >= 97 and temp <= 122): #for lowercase letter
                temp = temp - 97 #turns temp into a 0 to 25 value, each representing a letter of the english language.
                temp = 97 + (temp + (ord(key[modularj]) - 65)) % 26 #increments the temp value and converts back to ascii code.
                self.ciphertext += chr(temp) #converts ascii code to char.
                j = j + 1 #moves onto the next element of the key.
            elif(temp >= 65 and temp <= 90): #does the same as above for uppercase.
                temp = temp - 65 
                temp = 65 + (temp + (ord(key[modularj]) - 65)) % 26 
                self.ciphertext += chr(temp)
                j = j + 1
            else:
                self.ciphertext += i
            #j is only incremented if the current i is a letter of the alphebet. This preserves punctuation.

    def devigenere(self,key):
        j = 0
        key = key.upper()
        for i in self.text:
            modularj = j % len(key)
            temp = ord(i)
            if (temp >= 97 and temp <= 122):
                temp = temp - 97
                temp = 97 + (temp - (ord(key[modularj]) - 65)) % 26 #these lines are the only difference from vigenere()
                self.ciphertext += chr(temp)
                j = j + 1
                
            elif(temp >= 64 and temp <= 90):
                temp = temp - 65
                temp = 65 + (temp - (ord(key[modularj]) - 65)) % 26 #these lines are the only difference from vigenere()
                self.ciphertext += chr(temp)
                j = j + 1
            else:
                self.ciphertext += i  
#driver code for the actual encryption
def encrypt():
    enteringtext = True
    plaintext = ""
    print("Enter plaintext, an empty line with only ` to finish")
    while enteringtext:
        k = input("plaintext: ")
        if k == "`":
            break
        else:
            plaintext += k
    plaintext = encryption(plaintext,"")
        
    typeofencryption = input("Cipher type (caesar/vig/decaesar/devig): ")

    #why doesn't python not have switch statements
    if typeofencryption == "vig":
        plaintext.vigenere(input("key: "))
    elif typeofencryption == "caesar":
        plaintext.caesar(input("key: "))
    elif typeofencryption == "devig":
        plaintext.devigenere(input("key: "))
    elif typeofencryption == "decaesar":
        plaintext.decaesar(input("key: "))
    else:
        encrypt()
        return
    
    print(plaintext.ciphertext)

    return plaintext.ciphertext