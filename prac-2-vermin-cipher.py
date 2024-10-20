# vermin cipher02

pt = input("Enter plain text: ")
key = input("Enter key: ")

a = "abcdefghijklmnopqrstuvwxyz"

a1 = key.lower()  
for i in a:
    if i not in a1:
        a1 += i

print("Original Alphabet:", a)
print("Substitution Alphabet:", a1)
print('\n')


ct = ''
for i in pt:
    if i.lower() in a:  
        index = a.index(i.lower())  
        if i.isupper():
            ct += a1[index].upper()  
        else:
            ct += a1[index]  
    else:
        ct += i  

print('Plain Text:', pt)
print('Cipher Text:', ct)
