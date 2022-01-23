"""
存储全国各个城市的景区与美食，在控制台中显示出来.
北京∶
景区︰故宫，天安门,天坛.
美食:烤鸭,炸酱面，豆汁，卤煮.
四川:
景区︰九寨沟,峨眉山,春熙路·
美食:火锅，串串香，兔头.i
{“北京”：{“景区”:[故宫，天安门，天坛]}}  feature
"""
dict_toponymy={}
while True:
    toponymy=input("请输入一个地名:")
    if toponymy=="":
        break
    dict_toponymy_feature={}
    list_scenicspot=[]
    while True:
        scenicspot=input("请输入%s的景区:"%(toponymy))
        if scenicspot=="":
            break
        list_scenicspot.append(scenicspot)
    dict_toponymy_feature["景区"]=list_scenicspot
    list_cate=[]
    while True:
        cate=input("请输入%s的美食:"%(toponymy))
        if cate=="":
            break
        list_cate.append(cate)
    dict_toponymy_feature["美食"]=list_cate
    dict_toponymy[toponymy]=dict_toponymy_feature
for key,value in dict_toponymy.items():
    print(key+":")
    for i,j in value.items():
        print(i+":",end="")
        for jj in j:
            print(jj,end=" ")
        print()
