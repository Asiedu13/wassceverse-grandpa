import hashlib

str2hash = "sevenfromheaven"
result = hashlib.md5(str2hash.encode("utf-8")).hexdigest()
print(result)