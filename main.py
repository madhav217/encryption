import cipherclass as cipher

cipher.encrypt()

while True:
    i = input("end? (y/n) y to end, n to restart") 
    if i == "y":
        break
    elif i == "n":
        cipher.encrypt()
        