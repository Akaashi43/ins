#implementing MDA Algorithm4

import hashlib
result = hashlib.md5(b'Ismile') 
result1 = hashlib.md5(b'Esmile')  
print("The byte equivalent of hash is : ", end ="") 
print(result.digest()) 
print("The byte equivalent of hash is : ", end ="") 
print(result1.digest())
