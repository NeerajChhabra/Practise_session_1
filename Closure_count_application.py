

dict = {}




def outer(fn):
    c = 0
    def inner(*args, **kwargs):
        nonlocal c
        c += 1
        dict[fn.__name__] = c
        return fn(*args, **kwargs)
    return inner



def add(a, b):
    return a+b





def mult(a, b):
    return a*b




def div(a, b):
    return a/b





fn_add = outer(add)





fn_mult = outer(mult)




fn_div = outer(div)









