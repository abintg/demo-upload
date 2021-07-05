# import hashlib
# str=hashlib.sha1(b"abin")
# str2=str.hexdigest()
# print(str2)str2



import hashlib
hash_object = hashlib.sha224(b'Hello World')
hash_object = hashlib.sha256(b'Hello World')
hash_object = hashlib.sha384(b'Hello World')
hex_dig = hash_object.hexdigest()
print(hex_dig)