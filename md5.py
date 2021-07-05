import hashlib

def md5():
    a=str(input("enter your name:"))
    b=a.encode()
    c=hashlib.md5(b)
    hexa=c.hexdigest()
    print(hexa)
    return
md5()

# fc9d65365f1b36a2c1331dd54034c553

