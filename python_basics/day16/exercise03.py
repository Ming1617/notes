"""
    在列表中选出所有偶数
"""
list01=[4,5,43,45,123,44]

result=[]
for item in list01:
    if item%2==0:
        result.append(item)
print(result)

def get_even():
    for item in list01:
        if item % 2 == 0:
            yield item
g01=get_even()
for item in g01:
    print(item)