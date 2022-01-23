s="hello"# 字符串

s=b"hello"#字节串

print(s)

"""
所有字符串都能够转换为字节串
但是并不是所有的字节串能转换为字符串
"""

s="你好".encode() #将字符串转换为字节串
print(s)

# 将字节串 转换为 字符串
print(b'\xe4\xbd\xa0\xe5\xa5\xbd'.decode())
