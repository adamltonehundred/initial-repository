##Random Password
import random

i = 1
randPassword = ""

for i in range(1,12,1):
    charValue = random.randint(1,26)
    randChar = chr(96+int(charValue))
    randPassword = randPassword + randChar
    
print("Your password: ", randPassword)
