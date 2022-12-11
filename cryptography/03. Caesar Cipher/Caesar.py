# Filename: caesar.py 
def encrypt(text,s):  #Ενδέχεται να πρέπει να 
#διορθώσετε τον κώδικα – διαβάστε τα μηνύματα 
#σφάλματος (part of the excercice) 
    result = "" 
 
    for i in range(len(text)): 
        char = text[i] 
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65) 
        else: 
            result += chr((ord(char) + s - 97) % 26 + 97) 
    return result 
    
    text = "CEASER CIPHER DEMO" 
    s = 4 
    print ("Plain Text : " + text) #ίσως έχει σφάλμα 
    print ("Shift pattern : " + str(s)) 
    print ("Cipher: " + encrypt(text,s))

clear = "test example" 
encrypt(clear, "")