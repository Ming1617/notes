def fun01(a,b,c,d):
    print(a)
    print(b)
    print(c)
    print(d)
list01=['a','b','c','d']
fun01(*list01)
dict={"a":1,"c":3,"d":4,"b":2}
fun01(**dict)