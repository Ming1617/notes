def fun07(a, b, *args, c, d,**kwargs ) :
    print(a)
    print(b)
    print(args)
    print(c)
    print(d)
    print(kwargs)
fun07(1,2,123,23,2,c=1,d=4,e=1,f=2)