#def fun(*args):
#    return sum(args)
#print(fun(1, 2, 3, 4))
def fun(**kwargs):
    for k, val in kwargs.items():
        
        print(k, '=', val)
fun(a ='Python', b='is', c='awesome')