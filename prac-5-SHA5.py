#implementing SHA Algorithm5

from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random

def generate_signature(private_key, message): 
    key = RSA.importKey(private_key) 
    hashed_message = SHA256.new(message.encode('utf-8'))  
    signer = PKCS1_v1_5.new(key) 
    signature = signer.sign(hashed_message) 
    return signature 

def verify_signature(public_key, message, signature): 
    key = RSA.importKey(public_key) 
    hashed_message = SHA256.new(message.encode('utf-8')) 
    verifier = PKCS1_v1_5.new(key) 
    return verifier.verify(hashed_message, signature) 

random_generator = Random.new().read 
key_pair = RSA.generate(2048, random_generator) 

public_key = key_pair.publickey().export_key() 
private_key = key_pair.export_key() 

message = "Hello, World!" 

signature = generate_signature(private_key, message) 
print("Generated Signature:", signature.hex()) 

is_valid = verify_signature(public_key, message, signature) 
print("Signature Verification Result:", is_valid)
