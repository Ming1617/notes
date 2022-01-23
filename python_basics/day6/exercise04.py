"""
练习1:在控制台中循环录入商品信息(名称，单价).
如果名称输入空字符，则停止录入，
将所有信息逐行打印出来．

"""
dict_shoop={}
while True:
    key=input("请输入商品名称：")
    if key=="":
        break
    value=int(input("请输入商品单价："))
    dict_shoop[key]=value
for key,value in dict_shoop.items():
    print("%s的单价是%d"%(key,value))