import hashlib

md5 = hashlib.md5()
a = md5.update("gohome".encode("utf-8"))
print(md5.hexdigest())