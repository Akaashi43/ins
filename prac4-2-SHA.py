#implementing SHA Algorithm 

import hashlib 
str = input(" Enter the value to encode ") 
result = hashlib.sha1(str.encode()) 
print("The hexadecima equivalent if SHA1 is :  ") 
print(result.hexdigest())
