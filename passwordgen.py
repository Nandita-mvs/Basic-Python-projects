import random
import array

MAXLEN=12

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
LOWERCASE=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z'] 
UPPERCASE=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',  'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z'] 
SYMBOLS=['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<&# 039;'] 

COMBINEDLIST=DIGITS+LOWERCASE+UPPERCASE+SYMBOLS

randdig=random.choice(DIGITS)
randupper=random.choice(UPPERCASE)
randlower=random.choice(LOWERCASE)
randsym=random.choice(SYMBOLS)

temp=randdig+randupper+randlower+randsym

for x in range(MAXLEN-4):
    temp=temp+random.choice(COMBINEDLIST)

templist = list(temp)        # convert the string into a list of characters
random.shuffle(templist)     # shuffle the list of characters randomly
password= ''.join(templist)

print(password)




