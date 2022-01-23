import getpass
import hashlib

pwd=getpass.getpass("PW:")
print(pwd)

#hash对象
# hash=hashlib.md5()#生成对象

hash=hashlib.md5("*&#".encode())#算法加盐
hash.update(pwd.encode())#算法加密
pwd=hash.hexdigest()#提取加密后的密码
print(pwd)