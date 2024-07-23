def txt(text,n):
    ans = ""
    
    for i in range(len(text)):
        ch = text[i]
        
       
        if ch==" ":
            ans+=" "
       
        elif (ch.isupper()):
            ans += chr((ord(ch) + n-65) % 26 + 65)
        
        else:
            ans += chr((ord(ch) + n-97) % 26 + 97) 
    
    return ans

text=(input("Plain Text is : "))
n = int(input("Shift Text is : "))
print("Text : " + text)
print("Shift : " + str(n))
print("Cipher: " + txt (text,n))
