#partial function

from functools import partial

def mult(x,y) :
    return x*y

dbl = partial(mult, 2)
print(dbl(5))